from flask import Blueprint, request, jsonify

from bookmark import db
from bookmark.models import Book

books_resource = Blueprint('books', __name__)

@books_resource.route('', methods=['POST'])
def create():
    book = Book(**request.get_json())
    db.session.add(book)
    db.session.commit()
    return jsonify(book)


@books_resource.route('', methods=['GET'])
def list():
    return jsonify({
        'data': Book.query.all()
    })


@books_resource.route('<id>', methods=['GET'])
def get(id):
    book = Book.query.get(id)
    return jsonify(book)


@books_resource.route('<id>', methods=['PUT'])
def put(id):
    pass


@books_resource.route('<id>', methods=['DELETE'])
def delete(id):
    pass