#!/usr/bin/python3
"""
Module defining the route for API status check.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def index():
    """Route that returns the API status."""
    return jsonify({"status": "OK"})
