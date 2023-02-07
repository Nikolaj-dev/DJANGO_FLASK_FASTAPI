from app import app
from flask import jsonify
from models import Book
from flask import request
from app import db


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == "GET":
        books = Book.query.all()
        results = [
            {
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "price": book.price,
                "date_add": book.date_add,
                "status": book.status
            } for book in books
        ]
        return jsonify(results)

    elif request.method == "POST":
        if request.is_json:
            data = request.get_json()
            new_book = Book(
                title=data['title'],
                description=data['description'],
                price=data['price'],
                status=data['status']
            )
            db.session.add(new_book)
            db.session.commit()
            return {
                "message": f"Book {new_book.title} has been created.",
                "status": "200"
                }
        else:
            return {"error": "The request payload is not in JSON format."}


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def one_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == "GET":
        result = {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "price": book.price,
            "date_add": book.date_add,
            "status": book.status
        }
        return jsonify(result)

    elif request.method == "PUT":
        data = request.get_json()
        book.title = data['title']
        book.description = data['description']
        book.price = data['price']
        book.status = data['status']
        db.session.add(book)
        db.session.commit()
        return {
            "message": f"Book {book.title} has been updated.",
            "status": "200"
            }

    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return {
            "message": f"Book {book.title} has been deleted.",
            "status": "200"
            }


@app.after_request
def remove_header(response):
    del response.headers['X-Some-Custom-Header']

    return response
