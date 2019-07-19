import time

from sqlalchemy import Column, String, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    # passwd = Column(String(50))
    # admin = Column(Boolean())
    name = Column(String(50))

    # image = Column(String(500))
    # created_at = Column(Float(time.time))

    def __repr__(self):
        return "<User(name='%s', fullname='%s')>" % (
            self.name, self.email,)


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    user_name = Column(String(50))
    user_image = Column(String(500))
    name = Column(String(50))
    summary = Column(String(200))
    content = Column(Text())
    created_at = Column(Float(time.time))


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    blog_id = Column(String(50))
    user_id = Column(String(50))
    user_name = Column(String(50))
    user_image = Column(String(500))
    content = Column(Text())
    created_at = Column(Float(time.time))
