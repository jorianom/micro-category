from flask import Response, jsonify, request
from bson import json_util, ObjectId
from database import mongo
from datetime import datetime


def _create_category():
    data = request.get_json()
    name = data.get('name', None)
    if (name is None):
        return jsonify({'error': 'Name is required'}), 400
    creation_date = datetime.now()
    response = mongo.db.categories.insert_one({
        'name': name,
        'createTime': creation_date
    })
    return {'id': str(response.inserted_id)}, 201


def _get_categories():
    data = mongo.db.categories.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')


def _get_category(id):
    data = mongo.db.categories.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')


def _update_category(id):
    data = request.get_json()
    if len(data) == 0:
        return 'Invalid payload', 400

    response = mongo.db.categories.update_one(
        {'_id': ObjectId(id)}, {'$set': data})

    if response.modified_count >= 1:
        return 'Category updated successfully', 200
    else:
        return 'Category not found', 404


def _delete_category(id):
    response = mongo.db.categories.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'Category deleted successfully', 200
    else:
        return 'Category not found', 404
