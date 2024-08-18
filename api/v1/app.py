#!/usr/bin/python3
"""Flask application setup for AirBnB clone project."""
from models import storage
from flask import Flask, jsonify, make_response
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS

# Create a Flask instance
app = Flask(__name__)

# Set up CORS
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
# Allow all origins for development

# Register the blueprint app_views to the Flask instance
app.register_blueprint(app_views)


# Method to handle @app.teardown_appcontext
@app.teardown_appcontext
def teardown(self):
    """Calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors and returns a JSON response.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    # Run the Flask server
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
