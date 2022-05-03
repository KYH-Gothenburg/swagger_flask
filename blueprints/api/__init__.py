from flask import Blueprint, Response, request
import json

from blueprints.api.validations import check_id_format, check_book_keys
from db import books_db, get_book_by_id

bp_api = Blueprint('bp_api', __name__)


@bp_api.get('/books')
def get_books():
    return Response(json.dumps(books_db), 200, content_type='application/json')


@bp_api.get('/books/<id_>')
def get_book(id_):
    id_ = check_id_format(id_)
    if not id_:
        return Response(json.dumps({'Error': 'Id must be an integer'}), 400, content_type='application/json')

    book = get_book_by_id(id_)
    if book:
        return Response(json.dumps(book), 200, content_type='application/json')

    return Response(json.dumps({'Error': f'Book with id {id_} not found'}), 404, content_type='application/json')


@bp_api.post('/books')
def post_books():
    if not request.content_type == 'application/json':
        return Response(json.dumps({'Error:' f'Content-type must be application/json'}), 400, content_type='application/json')

    book = request.json

    response = check_book_keys(book)
    if response:
        return response

    id_ = books_db[-1]['id'] + 1
    book['id'] = id_

    books_db.append(book)
    return Response(json.dumps(book), 201, content_type='application/json')


@bp_api.put('/books/<id_>')
def put_books(id_):
    id_ = check_id_format(id_)
    if not id_:
        return Response(json.dumps({'Error': 'Id must be an integer'}), 400, content_type='application/json')

    # Get book from database
    book = get_book_by_id(id_)

    # If no book with this id exist, give an error message
    if not book:
        return Response(json.dumps({'Error': f'Book with id {id_} is not present in the database'}),
                        404, content_type='application/json')

    # We got the book from the database. Time to check the book data that came with the request
    if not request.content_type == 'application/json':
        return Response(json.dumps({'Error:' f'Content-type must be application/json'}),
                        400, content_type='application/json')

    request_book = request.json

    response = check_book_keys(request_book)
    if response:
        return response

    # The request book data was OK. Time to update the book with the id in the database
    request_book['id'] = book['id']
    index = books_db.index(book)
    books_db[index] = request_book

    return Response(json.dumps(request_book), 202, content_type='application/json')


@bp_api.delete('/books/<id_>')
def delete_book(id_):
    id_ = check_id_format(id_)
    if not id_:
        return Response(json.dumps({'Error': 'Id must be an integer'}), 400, content_type='application/json')

    # Get book from database
    book = get_book_by_id(id_)

    # If no book with this id exist, give an error message
    if not book:
        return Response(json.dumps({'Error': f'Book with id {id_} is not present in the database'}),
                        404, content_type='application/json')

    index = books_db.index(book)
    books_db.pop(index)

    return Response(json.dumps({'Success': f'Book with id {id_} was deleted'}), 200, content_type='application/json')

