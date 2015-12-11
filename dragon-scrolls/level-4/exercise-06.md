[Previous](exercise-05.md) |  [Next](exercise-07.md)
## Exercise 6: Add HTTP POST Support to our Web Service API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_05)

In a properly designed RESTful web service/api, we create new resources using
the POST HTTP method.  It's time for us to do that for our API so that we can 
create new friend records in our datastore.

> ![Question](../images/question.png) Review: What are the other common HTTP
methods (GET, PUT, PATCH, DELETE) used for in RESTful web services/apis?

### There Is No Secret Ingredient: [POST] A New Friend Today!
- Add the following function stubs to `friends.py` and `datastore.py`:
    ```python
    # friends.py
    @api.route('/api/v1/friends', methods=['POST'])
    def create_friend() -> flask.Response:
        """
        Create a new friend resource. 
        
        Utilize a JSON representation in the request object to create
        a new friend resource.
        """
        pass
        
    # datastore.py
    def create_friend(data: dict):
        """
        Create a new friend entry is our datastore of friends.
    
        Args:
            data: A dictionary of data for our new friend.
        """
        _friends.append(data)
    ```

- The first thing our `friends.create_friend` function needs to do is get access 
to the JSON in the HTTP request in order to construct a new friend resource.  
You can do so by replacing `pass` with the following code:

    ```python
    request_payload = flask.request.get_json()
    ```
    - The `request` object is a special variable whose value is 
    always bound to the current HTTP request being handled by the program. 
         
- Now that you have the JSON payload, you pass that along to the  
`datastore.create_friend` function to create the new resource. Then wrap up
the function by returning a success message to the client:

    ```python
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
    ```
    
    - Notice here how we delegate from `friends.create_friend` to 
    `datastore.create_friend` to actually add the friend to our list.
    
    - Also, note how we also use `make_response` here to override
    the standard `200` response code with `201` which means a new resource
    was successfully created.
    
### There Is No Secret Ingredient: Testing
Let's take our new functionality for a test.
- From your secondary terminal window issue the following command: 

    ```bash
    curl 127.0.0.1:5000/api/v1/friends -X POST -H "content-type:application/json" -d '{"id":"dDuck", "firstName": "Donald", "lastName": "Duck", "telephone": "i-love-ducks", "email": "donald@disney.com", "notes": "A grumpy, easily agitated duck."}'
    ```
    
    > ![info](../images/information.png) `-X` allows you to specify which HTTP method to use.
    
    > ![info](../images/information.png) `-H` allows you to specify HTTP headers and values.
    
    > ![info](../images/information.png) `-d` allows you to specify the data to pass in the payload.

- This is the response that you should get back:
    
    ```
    {
      "message": "Friend resource created."
    }
    ```
    
### Oh Crapola! You've Got Major Bugs
If you've been following along very precisely, everything should have worked
up to this point.  However, we actually been introducing bugs into our program
along the way.  Here are some of them:
    
- If you leave out the request header that sets `content-type` to `application/json` 
your API will create a `null` friend in `datastore.friends`.
 
- Have a syntax error in the JSON payload?  You'll get a strange HTML error 
message with a 400 status code from your API.

- You can create friends with missing data elements.

- You can create multiple friends with the same ID.

It's time to **squash some bugs!**

| [Next Exercise](exercise-07.md)
