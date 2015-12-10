"""
This module will provide a Flask application.
"""

import flask

from friends_api import datastore


api = flask.Flask(__name__)