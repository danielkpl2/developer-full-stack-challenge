from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Request, Response, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy import select, asc
from schema import (
    Author,
    AuthorBase,
    AuthorCreate,
    AuthorUpdate,
    BookBase,
    Book,
    BookCreate,
    BookUpdate,
    UserBase,
    Token,
)
from models import Author as AuthorModel
from models import Book as BookModel
from models import User as UserModel
from auth import get_current_user, login_for_access_token, oauth2_scheme
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi_pagination import Page, add_pagination, LimitOffsetPage

from fastapi_pagination.ext.sqlalchemy import paginate

import os
from dotenv import load_dotenv

load_dotenv(".env")

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
DEV_URL = os.getenv("DEV_URL", "http://localhost:3000/")

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# Add the default CORS middleware for handling CORS headers on other requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict origins to a list of trusted domains
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# If in production then serve the nuxt generated html file (presume it exists).
# This is ignoring SSR and the separate docker container.
# In dev this would redirect to the dashboard url whether it's local or dockerized.

if ENVIRONMENT == "prod":
    app.mount("/", StaticFiles(directory="../dashboard/dist", html=True), name="static")
# if in dev then redirect to the nuxt dev server
elif ENVIRONMENT == "dev":

    @app.get("/")
    def read_root():
        return RedirectResponse(DEV_URL)


@app.get("/authors", response_model=LimitOffsetPage[Author])
async def authors(
    token: Annotated[str, Depends(oauth2_scheme)],
    limit: int,
    offset: int,
    search: str = "",
) -> LimitOffsetPage[Author]:
    return paginate(
        db.session,
        select(AuthorModel)
        .filter(AuthorModel.name.ilike(f"%{search}%"))
        .order_by(asc(AuthorModel.id)),
    )


@app.post("/authors", response_model=Author)
async def create_author(
    token: Annotated[str, Depends(oauth2_scheme)], author: AuthorCreate
) -> Author:
    new_author = AuthorModel(name=author.name)
    db.session.add(new_author)
    db.session.commit()
    db.session.refresh(new_author)
    return new_author


@app.patch("/authors/{author_id}", response_model=Author)
async def update_author(
    token: Annotated[str, Depends(oauth2_scheme)], author_id, author: AuthorUpdate
) -> Author:
    updated_author = db.session.query(AuthorModel).get(author_id)
    updated_author.name = author.name
    db.session.commit()
    db.session.refresh(updated_author)
    return updated_author


@app.get("/books", response_model=LimitOffsetPage[Book])
async def books(
    token: Annotated[str, Depends(oauth2_scheme)],
    limit: int,
    offset: int,
    search: str = "",
    author_id: int = None,
) -> LimitOffsetPage[Book]:
    query = select(BookModel).filter(BookModel.name.ilike(f"%{search}%"))
    if author_id is not None:
        query = query.filter(BookModel.author_id == author_id)
    sorted_books = paginate(db.session, query.order_by(asc(BookModel.id)))
    return sorted_books


@app.post("/books", response_model=Book)
async def create_book(token: Annotated[str, Depends(oauth2_scheme)], book: BookCreate) -> Book:
    new_book = BookModel(
        name=book.name, number_pages=book.number_pages, author_id=book.author_id
    )
    db.session.add(new_book)
    db.session.commit()
    db.session.refresh(new_book)
    return new_book


@app.patch("/books/{book_id}", response_model=Book)
async def update_book(
    token: Annotated[str, Depends(oauth2_scheme)], book_id, book: BookUpdate
) -> Book:
    updated_book = db.session.query(BookModel).get(book_id)
    updated_book.name = book.name
    updated_book.number_pages = book.number_pages
    updated_book.author_id = book.author_id
    db.session.commit()
    db.session.refresh(updated_book)
    return updated_book


@app.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: Annotated[UserModel, Depends(get_current_user)]):
    user = UserBase(username=current_user.username)
    return user


@app.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login_for_access_token(form_data)


add_pagination(app)
