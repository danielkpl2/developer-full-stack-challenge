from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema import Author, AuthorBase, AuthorCreate, BookBase, Book, UserBase, Token
from models import Author as AuthorModel
from models import Book as BookModel
from models import User as UserModel
from auth import get_current_user, login_for_access_token

import os
from dotenv import load_dotenv
load_dotenv('.env')

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
DEV_URL = os.getenv("DEV_URL", "http://localhost:3000/")

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


# If in production then serve the nuxt generated html file (presume it exists).
# This is ignoring the separate docker for the dashboard as it wouldn't be used in production.
# In dev this would redirect to the dashboard url whether it's local or dockerized. 

if ENVIRONMENT == "prod":
    app.mount("/", StaticFiles(directory="../dashboard/dist", html=True), name="static")
# if in dev then redirect to the nuxt dev server
elif ENVIRONMENT == "dev":
    @app.get("/")
    def read_root():
        return RedirectResponse(DEV_URL)


@app.get("/authors", response_model=list[Author])
async def authors():
    authors = db.session.query(AuthorModel).all()
    authors_with_number_books = [
        Author(id=author.id, name=author.name, number_books=author.number_books)
        for author in authors
    ]
    return authors_with_number_books


@app.get("/books", response_model=list[Book])
async def books():
    books = db.session.query(BookModel).all()
    return books


@app.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: Annotated[UserModel, Depends(get_current_user)]):
    user = UserBase(username=current_user.username)
    return user


@app.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login_for_access_token(form_data)


