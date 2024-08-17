#!/usr/bin/python3
"""Handles default RESTful API actions for State objects"""
from models import storage
from api.v1.views import app_views
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    """Retrieves the list of all State objects"""
    return jsonify([state.to_dict() for state in storage.all(State).values()])


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state_by_id(state_id):
    """Retrieves a State object by its ID"""
    state_by_id = storage.get(State, state_id)
    if state_by_id is None:
        abort(404)
    return jsonify(state_by_id.to_dict())


@app_views.route('/states/<state_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object by its ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()  # Persist the deletion
    return jsonify({}), 200  # Return an empty dictionary with status code 200


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def create_state():
    """Creates a new State"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    state_data = request.get_json()
    new_state = State(**state_data)
    new_state.save()

    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    """Updates a State object by its ID"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)

    state.save()
    return jsonify(state.to_dict()), 200
