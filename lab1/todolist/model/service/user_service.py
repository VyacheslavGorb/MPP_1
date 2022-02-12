import bcrypt

from todolist.model.models import User
from todolist.model.models import db


def login_available(login):
    user = User.query.filter_by(login=login).first()
    return user is None


def insert_user(login: str, password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes(password, 'latin-1'), salt)
    db.session.add(User(login=login, password=hashed_password))
    db.session.commit()


def is_valid_credentials(login: str, password: str):
    user = User.query.filter_by(login=login).first()
    if not user:
        return False
    return bcrypt.checkpw(bytes(password, 'latin-1'), user.password)
