from .books import books_resource
from .auth import auth_resource, jwt

__ALL__ = [jwt, books_resource, auth_resource]