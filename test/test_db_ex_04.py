import pytest
from exercise_04.setup_db import User, Post, Tag, prepare_session, delete_db_file, populate_db


@pytest.fixture(scope="function")
def session_with_empty_db():
    delete_db_file()
    yield prepare_session()
    delete_db_file()


@pytest.fixture(scope="function")
def session_with_populated_db():
    delete_db_file()
    session = prepare_session()
    populate_db(session())
    yield prepare_session()
    delete_db_file()


def test_add_user_to_db(session_with_empty_db):
    user = User(name='Alexey Smirnov',
                email='smirnov@gmail.com',
                password='rTy78E$')
    session = session_with_empty_db()
    session.add(user)
    session.commit()
    user_from_db = session.query(User).filter_by(name='Alexey Smirnov').first()
    assert (user_from_db.name, user_from_db.email, user_from_db.password) == (
        'Alexey Smirnov', 'smirnov@gmail.com', 'rTy78E$')


def test_get_posts_created_by_user(session_with_populated_db):
    session = session_with_populated_db()
    user = session.query(User).filter_by(name='Anton Klyukin').first()
    assert len(user.posts) == 2


def test_get_post(session_with_populated_db):
    session = session_with_populated_db()
    post = session.query(Post).filter_by(id=1).first()
    assert post.title == 'Первый пост о настольных варгеймах'


def test_get_tags_of_post(session_with_populated_db):
    session = session_with_populated_db()
    post = session.query(Post).filter_by(title='Первый пост о настольных варгеймах').first()
    assert len(post.tags) == 3


def test_add_tag_to_post(session_with_populated_db):
    session = session_with_populated_db()
    tag = Tag(name='Vietnam War')
    session.add(tag)
    session.commit()
    post = session.query(Post).filter_by(title='Пост об игре The Dark Sands').first()
    post.tags.append(tag)
    session.commit()
    assert len(post.tags) == 1
