[Previous](exercise-07.md) |  [Next](exercise-09.md)
## Exercise 8: Adding HTTP PATCH Support in our Web Service API
I hope that you are starting to get the hang of adding functionality to your
API by now.  In this exercise, we'll be adding the ability to update
existing friend resources.

### There Is No Secret Ingredient: Creating an `update_friend` function in 
`friends` and `datastore` modules.

Here's what the functions should look like:

```python
# friends.py
@api.route('/api/v1/friends/<id>', methods=['PATCH'])
def update_friend(id: str) -> flask.Response:
    """
    Update an existing friend resource.

    Utilize a JSON representation/payload in the request object to
    updated an existing friend resource.

    Args:
        id: The unique ID value of a given friend.

    Returns:
        A flask.Response object.
    """
    try:
        request_payload = flask.request.get_json()
    except BadRequest as error:
        response = flask.make_response(
            flask.jsonify({"error": "JSON payload contains syntax errors. "
                           "Please fix and try again."}),
            400)
        return response

    try:
        datastore.update_friend(id, request_payload)
    except ValueError as error:
        response = flask.make_response(
            flask.jsonify({"error": str(error)}),
            400)
        return response
    else:
        response = flask.make_response(
            flask.jsonify({"message": "Friend resource updated."}), 200)
        return response
    
# datastore.py
def update_friend(id: str, data: dict):
    """
    Update an existing friend entry is our datastore of friends.

    Args:
        data: A dictionary of data to update an existing friend entry with.

    Raises:
        ValueError: If data is None or if no matching friend entry is found.
    """
    if data is None:
        raise ValueError(
            "`None` was received when a dict was expected during "
            "the attempt to update an existing friend resource.")

    try:
        friend(id).update(data)
    except AttributeError:
        raise ValueError(
            "No existing friend was found matching id: {}".format(id))
```

- There is a substantial amount of similarity between `friends.create_friend()`
and `friends.update_friend()`.

    - In the function decorator, we are using the same URL template as we did for 
    `specific_friend`.  We've modified the `methods` parameter to indicate
    that the decorated function should handle `PATCH` HTTP requests. PATCH 
    requests will route to this new method, while `GET` requests to the 
    same url will route to `specific_friend`.  Pretty cool!
    
        - Also notice that we are also capturing the `<id>` portion of the url and
        passing it `datastore.update_friend`.
    
    - Just like before, we are checking for a `BadRequest` exception to
    be raised from `flask.request.get_json()`.
    
    - Instead of calling `datastore.create_friend()` we call 
    `datastore.update_friend()`.  We still check for `ValueError` 
    exceptions from this call and return 400 errors if the arise.
    
    > Notice how there is a separate exception clause?
    START HERE
    
    - Otherwise, we construct a response and return it.  Notice that we
    don't have to use `make_response` because the default 200 status code
    is appropriate in this case.

- There is also a significant degree of crossover between 
`datastore.update_friend` and `datastore.create_friend`.
    
    - We don't check to see if all the elements of a new friend entry are in 
    the payload.  This is unnecessary because the nature of a `PATCH` update
    is to allow for variable updates of an existing resource.  Requiring that
    all data elements of a record be present in the request would mean that
    we would only allow full updates of existing resources.

    - You may have except and `if/else` construct to be used here and by surprised
    that we've used `try/except` instead.
        - As a general practice, the Python community embraces an "it's easier
        to ask forgiveness than permission" type of programming style.  This
        is in contrast to a "look before you leap" style.
        
        - We could have written the same functionality like this:
        
            ```python
            ...
            if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to update an existing friend resource.")
    
            matched_friend = friend(id)
            if matched_friend:
                matched_friend.update(data)
            ...
            ```
    
    > ![Extra Info](../images/information.png) The `update` method of `dict`
    > objects can take another `dict` as an argument.  If matching keys are
    > found on two dictionary objects, the values from the 2nd dictionary replace
    > the values of the first dictionary for the corresponding key.  If new
    > keys are present in the second dictionary, these are added to the first
    > dictionary with their corresponding values.
    >
    > Further Reading(https://docs.python.org/3.5/library/stdtypes.html#dict.update)

    
### There Is No Secret Ingredient: Testing
Let's verify that our new code works as expected.  Here are some tests and what
you should get back from each command:

* Try to update the `BFP` friend resource:
    
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'  
    {
      "message": "Friend resource updated."
    }
    ```

* Make a call without the `content-type` header:

    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -d '{"id":"bfp", "firstName": "Really Really Fat", "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    {
      "error": "No JSON payload present.  Make sure that appropriate 
      `content-type` header is included in your request and that you've 
       specified a payload."
    }
    ```
    
* Make a call with a syntax error: 
    ```bash
    >>> curl 127.0.0.1:5000/api/v1/friends/bfp -X PATCH -H "content-type:application/json" -d '{"id":"bfp", "firstName": "Really Really Fat" "lastName": "Panda", "telephone": "i-love-tacos", "email": "mike@eikonomega.com", "notes": "A Panda.  Getting fatter pound at a time."}'
    
    {
      "error": "JSON payload contains syntax errors. Please fix and try again."
    }
    ```
        
| [Next Exercise](exercise-09.md)


       
        
