#!/usr/bin/python3
"""
Blueprint setup for API views.
"""
from flask import Blueprint

# Create a Blueprint instance with a URL prefix
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import all routes from index (PEP8 will complain)
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
