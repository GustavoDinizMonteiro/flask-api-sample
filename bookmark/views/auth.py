from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token
)

from bookmark import db
from bookmark.models import User

jwt = JWTManager()
bcrypt = Bcrypt()
auth_resource = Blueprint('auth', __name__)

class AuthUser:
    def __init__(self, id, email):
        self.id = id
        self.email = email

@jwt.user_identity_loader
def add_claims_to_access_token(user):
    return user.id


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return User.query.get(user.id)


# @auth_resource.route('/test', methods=['POST'])
# @jwt_required
# def test():
#     return jsonify({
#         'current_identity': get_jwt_identity(),
#         'current_roles': get_jwt_claims()
#     })

@auth_resource.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()
    print(bcrypt.check_password_hash(user.password, password))
    if user is None or not bcrypt.check_password_hash(user.password, password):
        return jsonify({ 'msg': 'Bad credentials' }), 401

    auth_user = AuthUser(user.id, user.email)

    return jsonify({
        'token': create_access_token(auth_user)
    })


@auth_resource.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(email, bcrypt.generate_password_hash(password).decode('utf-8'))
    db.session.add(user)
    db.session.commit()
    return jsonify(AuthUser(user.id, user.email).__dict__)