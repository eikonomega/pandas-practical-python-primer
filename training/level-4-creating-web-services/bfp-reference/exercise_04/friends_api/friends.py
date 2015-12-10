"""
This module will provide a Flask application.
"""

import flask

from friends_api import datastore


api = flask.Flask(__name__)


@api.route('/api/v1/friends', methods=['GET'])
def get_friends() -> flask.Response:
    """
    Return a representation of the collection of friend resources.

    Returns:
        A flask.Response object.
    """
    friends_list = datastore.friends()
    return flask.jsonify({"friends": friends_list})
