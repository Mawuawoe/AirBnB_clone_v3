#!/usr/bin/python3
"""
Flask application setup for AirBnB clone project.
"""
from flask import Flask
from os import getenv
from models import storage
from api.v1.views import app_views

# Create a Flask instance
app = Flask(__name__)

# Register the blueprint app_views to the Flask instance
app.register_blueprint(app_views)


# Method to handle @app.teardown_appcontext
@app.teardown_appcontext
def teardown(self):
    """Calls storage.close()"""
    storage.close()


if __name__ == "__main__":
    # Run the Flask server
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
