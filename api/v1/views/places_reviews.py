#!/usr/bin/python3
"""Handles default RESTful API actions for Review objects"""
from models import storage
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.user import User
from flask import jsonify, abort, request


@app_views.route('/places/<place_id>/reviews', strict_slashes=False)
def get_reviews(place_id):
    """Retrieves the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = place.reviews
    return jsonify([review.to_dict() for review in reviews])


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def get_review_by_id(review_id):
    """Retrieves a Review object by its ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>',
                 strict_slashes=False,
                 methods=['DELETE'])
def delete_review(review_id):
    """Deletes a Review object by its ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 strict_slashes=False,
                 methods=['POST'])
def create_review(place_id):
    """Creates a new Review"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if 'text' not in data:
        abort(400, description="Missing text")

    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)

    data['place_id'] = place_id
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', strict_slashes=False, methods=['PUT'])
def update_review(review_id):
    """Updates a Review object by its ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()
    for key, value in data.items():
        if key not in ['id',
                       'user_id',
                       'place_id',
                       'created_at',
                       'updated_at']:
            setattr(review, key, value)

    review.save()
    return jsonify(review.to_dict()), 200
