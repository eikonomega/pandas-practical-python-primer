[Previous](exercise-04.md) |  [Next](exercise-06.md)
## Exercise 5: Additional HTTP GET Support to your API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_04)

In this exercise you will add support for retrieving a specific friend 
resource representations from your API.

### There Is No Secret Ingredient: [GET] One Specific Friend
- Let's start by adding a new function to the `datastore` module
that will return information on a single friend based on a `id` parameter:

    ```python
    def friend(id: str) -> dict:
        """
        Provide data on a single friend.
        
        Args:
            id: A str of the unique identifier to look for in our list of friends. 
    
        Returns:
            A dict of data on the designated fried or None if not match is found.
        """
        for possible_match in _friends:
            if id == possible_match['id']:
                return possible_match
    ```
    
    - This function iterates of our list of `_friends` and sees if there
    is friend with an `id` key the value of which is equal to the `id` 
    parameter passed into the function.
    
    - If so, the matching friend entry is returned.  Otherwise `None` is 
    returned from the function since no other value is explicitly returned.

- With that in place, let's make a corresponding `friend` function in the 
`friends.py` module:

    ```python
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
            original_response = flask.jsonify(
                {"error": "No friend found with the specified identifier."})       
            error_response = flask.make_response(
                original_response, 404)     
            return error_response
    ```

- Notice that in the `@api.route` decorator of our new function that there 
is a `<id>` added to the end of the URL.  Whenever a segment of the URL is
enclosed in `<>`, Flask will capture the that portion of the URL and 
pass it to your function as a variable named whatever was inside the `<>`. 
    - In this case, it passes `id` into our function. In a real request,
    let's say to `www.yourserver.com/api/v1/friends/BFP`, `BFP` would be
    sent to our function as the variable `id`.
    
- If a matching friend is found in the call to `datastore.friend`, we return 
just that single friend record to the client by passing it to `flask.jsonify`.

- If no matching friend is found however, we need to return a different type 
of response to the client - with a different HTTP status code in particular.  
In order to do this, we make use of the `flask.make_response` function.

    - This function allows us to take another flask.Response object as the 
    first parameter, and then modify its status code with the second parameter.
    
    - In this case, you can see that we first create a normal JSON 
     response and assign it to `original_response`. 
       
    - We then pass this object as the first parameter to `make_response`. 
    
    - Then as the second parameter, we pass a override status code, that will
    replace the default `200 OK` status code on the `jsonify` response object.
    
    > ![Alternative Approach](../images/information.png You it isn't necessary
    > to put the call to `flask.jsonify` in a separate statement from 
    > `flask.make_response`.  You could just put the call to `flask.jsonify`
    >  as the first argument to `make_response`:
    >
    >    ```python
    >    ...
    >    error_response = flask.make_response(
    >        flask.jsonify({"error": "No friend found with the specified identifier."}),
    >        404)
    >    ...
    >    ```

- Finally, we return the modified reponse object.

> ![Question](../images/question.png) What are we changing the HTTP status code
> to?  Why is that important?

> ![Extra Extra](../images/reminder.png) Notice how we've been explicit about
> what HTTP status codes can be returned from our new function? Users of 
> your API will appreciate this level of detail.

### There Is No Secret Ingredient: Testing
- Drop to the command-line and try to access your new method: 
`curl 127.0.0.1:5000/api/v1/friends/VinDi`.  You should get the following
output:
    
    ```JSON
    {
      "email": "vdiesel4@supercool.edu",
      "firstName": "Vin",
      "id": "VinDi",
      "lastName": "Diesel",
      "notes": "Really annoying guy.  Will never amount to anything.",
      "telephone": "I-HIT-PEOPLE"
    }
    ```

> ![Alert](../images/alert.png) We've introduced a bug here that might not be
> be immediately obvious.  What happens when we query for `BFP`?  What about
> `bfp`?  Our API doesn't account for differences in capitalization.  Go
> back and review [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) 
> to see how to make your API find your >BFP friend whether the input is 
> `BFP`, `bfp`, of `bFp`.

| [Next Exercise](exercise-06.md)
