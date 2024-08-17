#!/usr/bin/python3
"""Handles default RESTful API actions for City objects"""
from models import storage
from api.v1.views import app_views
from models.state import State
from models.city import City
from flask import jsonify, abort, request, make_response


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def get_cities(state_id):
    """Retrieves the list of all City objects of a specific State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object by its ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def delete_city(city_id):
    """Deletes a City object by its ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()  # Persist the deletion
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['POST'])
def create_city(state_id):
    """Creates a new City within a specific State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    city_data = request.get_json()
    if 'name' not in city_data:
        abort(400, description="Missing name")

    city_data['state_id'] = state_id
    new_city = City(**city_data)
    new_city.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def update_city(city_id):
    """Updates a City object by its ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")

    city_data = request.get_json()
    for key, value in city_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)

    city.save()
    return jsonify(city.to_dict()), 200
