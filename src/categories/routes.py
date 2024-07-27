from flask import Blueprint
from flask_cors import CORS
from flask_cors import cross_origin

from categories.controller import _create_category, _get_categories, _get_category, _update_category, _delete_category

categories = Blueprint('categories', __name__)


@categories.route('/', methods=['GET'])
def get_categories():
    return _get_categories()


@categories.route('/<id>', methods=['GET'])
def get_category(id):
    return _get_category(id)


@categories.route('', methods=['POST'])
@cross_origin()
def create_category():
    return _create_category()


@categories.route('/<id>', methods=['PUT'])
def update_category(id):
    return _update_category(id)


@categories.route('/<id>', methods=['DELETE'])
@cross_origin()
def delete_category(id):
    return _delete_category(id)
