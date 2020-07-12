from flask import Blueprint, request, jsonify
from passlib.hash import pbkdf2_sha256

from bookmark import db
from bookmark.models import User

users_resource = Blueprint('users', __name__)


@users_resource.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(email, pbkdf2_sha256.hash(password))
    db.session.add(user)
    db.session.commit()
    return jsonify(user)