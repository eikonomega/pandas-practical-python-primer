"""
This module will provide a Flask application.
"""

import flask

from friends_api import datastore


api = flask.Flask(__name__)


@api.route('/api/v1/friends', methods=['GET'])
def friends() -> flask.Response:
    """
    Return a representation of the collection of friend resources.

    Returns:
        A flask.Response object.
    """
    friends_list = datastore.friends()
    return flask.jsonify({"friends": friends_list})


@api.route('/api/v1/friends/<id>', methods=['GET'])
def friend(id: str) -> flask.Response:
    """
    Return a representation of a specific friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object with two possible status codes:
            200: A friend resource was found and returned.
            404: No matching friend resource was found.
    """
    matched_friend = datastore.friend(id)
    if matched_friend:
        return flask.jsonify(matched_friend)

    else:
        # Equivalent, but more verbose.
        # original_response = flask.jsonify(
        #     {"error": "No friend found with the specified identifier."})
        # error_response = flask.make_response(
        #     original_response, 404)
        # return error_response

        error_response = flask.make_response(
            flask.jsonify(
                {"error": "No friend found with the specified identifier."}),
            404)
        return error_response


@api.route('/api/v1/friends', methods=['POST'])
def create_friend() -> flask.Response:
    """
    Create a new friend resource.

    Utilize a JSON representation in the request object to create
    a new friend resource.
    """
    request_payload = flask.request.get_json()

    datastore.friends.append(request_payload)

    response = flask.make_response(
            flask.jsonify({"message": "Friend resource created."}), 201)
    return response