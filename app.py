from flask import Flask, request, jsonify
from models import Book, initialize_db

app = Flask(__name__)

@app.before_request
def before_request():
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    db.close()

@app.route('/books', methods=['POST'])
def add_book():
    book = Book.create(**request.get_json())
    return jsonify(book.to_dict()), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.select()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.get(Book.id == id)
    book.delete_instance()
    return '', 204
