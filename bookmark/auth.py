from passlib.hash import pbkdf2_sha256

from bookmark.models import User

def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)