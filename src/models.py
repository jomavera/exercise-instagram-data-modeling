import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    content = Column(String(250))
    url_image = Column(String(205),nullable=False)
    date = Column(Date,nullable=False)

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.id'))
    content = Column(String(250))
    date = Column(Date, nullable=False)


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey('post.id'))
    userId = Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e