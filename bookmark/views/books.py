from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required

from bookmark import db
from bookmark.models import Book

books_resource = Blueprint('books', __name__)

@books_resource.route('', methods=['POST'])
@jwt_required()
def create():
    book = Book(**request.get_json())
    db.session.add(book)
    db.session.commit()
    return jsonify(book)


@books_resource.route('', methods=['GET'])
def list():
    pass


@books_resource.route('<id>', methods=['GET'])
def get(id):
    pass


@books_resource.route('<id>', methods=['PUT'])
def put(id):
    pass


@books_resource.route('<id>', methods=['DELETE'])
def delete(id):
    pass