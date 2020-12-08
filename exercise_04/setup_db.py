#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.sqltypes import DateTime

from datetime import datetime
import os.path
import pathlib

DB_FILE_NAME = 'my_blog.sqlite'

DB_PATH = os.path.join(pathlib.Path().absolute(), 'db', DB_FILE_NAME)

engine = create_engine(f'sqlite:///{DB_PATH}')

Base = declarative_base(bind=engine)

posts_tags_assoc_table = Table(
    'posts_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(),
                        default=datetime.now,
                        onupdate=datetime.now)

    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return (f"<User(name='{self.name}', email='{self.email}',"
                f" password='{self.password}')>")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(),
                        default=datetime.now,
                        onupdate=datetime.now)

    user = relationship("User", back_populates='posts')
    tags = relationship('Tag',
                        secondary=posts_tags_assoc_table,
                        back_populates='posts')

    def __repr__(self):
        return f"<Post(title='{self.title[:10]}')>"


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    posts = relationship('Post',
                         secondary=posts_tags_assoc_table,
                         back_populates='tags')

    def __repr__(self):
        return f"<Tag(name={self.name})>"


def delete_db_file():
    if os.path.isfile(DB_PATH):
        os.remove(DB_PATH)


def populate_db(session):
    user_01 = User(name='Anton Klyukin',
                   email='antonklyukin@gmail.com',
                   password='k6FuSD#')
    user_02 = User(name='John Doe',
                   email='doe@hotmail.com',
                   password='HNDsf09')
    user_03 = User(name='Octavian August',
                   email='august@rome.com',
                   password='Kjp9023')

    session.add_all((user_01, user_02, user_03))
    session.flush()

    post_01 = Post(title='Первый пост о настольных варгеймах',
                   text='Это первый пробный пост о настольных варгеймах.',
                   author_id=user_01.id)

    post_02 = Post(title='Пост об игре The Dark Sands',
                   text='Dark Sands - настольная игра о войне в Северной Африке в 1941-1942 гг.',
                   author_id=user_01.id)

    session.add_all((post_01, post_02))
    session.flush()

    tag_01 = Tag(name='Wargames')
    tag_02 = Tag(name='GMT Games')
    tag_03 = Tag(name='Rommel')

    session.add_all((tag_01, tag_02, tag_03))
    session.flush()

    post_01.tags.extend((tag_01, tag_02, tag_03))

    session.commit()

    print(post_01.tags)
    print(post_02.user)

    user = session.query(User).filter_by(name='Alexey Smirnov').first()
    print(user)

    session.close()


def prepare_session():
    Base.metadata.create_all()
    return sessionmaker(bind=engine)
