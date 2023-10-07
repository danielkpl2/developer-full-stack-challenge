from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
Base  = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id  = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='author')

    @hybrid_property
    def number_books(self):
        return len(self.books)
    

class Book(Base):
    __tablename__ = 'book'
    id  = Column(Integer, primary_key=True)
    name = Column(String)
    number_pages = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', back_populates='books')


class User(Base):
    __tablename__ = 'dcuser'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
