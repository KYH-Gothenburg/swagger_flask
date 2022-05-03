import json

from flask import Response


def check_id_format(id_):
    """
    Check that id_ string only contains digits and convert it to an int if it does
    :param id_: Book id as a numeric string
    :return: id_ as an int or None
    """
    if id_.isdigit():
        return int(id_)

    return None


def check_book_keys(book):
    """
    Check that the keys in the book dict is correct
    :param book: A book dict
    :return: None if no errors, or a Response object if an error is found
    """
    accepted_keys = ['title', 'author', 'description']

    # Check that the keys provided in the json request belongs to one of the accepted keys
    for key in book:
        if key not in accepted_keys:
            return Response(json.dumps({'Error': f'The key {key} is not accepted in the json request'}),
                            400,
                            content_type='application/json')

    # Check that all accepted keys are present in the request
    for key in accepted_keys:
        if key not in book:
            return Response(json.dumps({'Error': f'The required key {key} is not present in the json request'}),
                            400,
                            content_type='application/json')

    return None
