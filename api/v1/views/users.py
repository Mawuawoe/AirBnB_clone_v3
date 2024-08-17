#!/usr/bin/python3
"""Handles default RESTful API actions for User objects"""
from models import storage
from api.v1.views import app_views
from models.user import User
from flask import jsonify, abort, request


@app_views.route('/users', strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])


@app_views.route('/users/<user_id>', strict_slashes=False)
def get_user_by_id(user_id):
    """Retrieves a User object by its ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """Deletes a User object by its ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()  # Persist the deletion
    return jsonify({}), 200


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def create_user():
    """Creates a new User"""
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")

    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    """Updates a User object by its ID"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)

    user.save()
    return jsonify(user.to_dict()), 200
