from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorCreate):
    id: int

class Author(AuthorBase):
    id: int
    number_books: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    name: str
    number_pages: int

class BookCreate(BookBase):
    author_id: int

class BookUpdate(BookCreate):
    id: int

class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None