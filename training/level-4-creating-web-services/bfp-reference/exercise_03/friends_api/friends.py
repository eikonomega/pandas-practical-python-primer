"""
This module will provide a Flask application.
"""

from flask import Flask

from friends_api import datastore


app = Flask(__name__)