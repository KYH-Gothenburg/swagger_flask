books_db = [
    {
        'id': 1,
        'title': 'A very good book',
        'author': 'Anna Good',
        'description': 'Some description'
    },
    {
        'id': 2,
        'title': 'A very bad book',
        'author': 'Bob Bad',
        'description': 'Some other description'
    },
]


def get_book_by_id(id_):
    """
    Get a book by its id
    :param id_: Id of requested book
    :return: book dict or None
    """
    for book in books_db:
        if book['id'] == id_:
            return book
    return None
