[Previous](exercise-03.md) |  [Next](exercise-05.md)
## Exercise 4: Adding HTTP GET Support to your API
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_03)

The first thing that we are going to do is add support for HTTP GET operations
to our API.  In this exercise, we will add it for the **resource collection** 
and in the next exercise will add it for **individual resources**.

> ![Question](../images/question.png) Do you remember what the difference 
> is between those two terms and how their URLs might differ?

### There Is No Secret Ingredient: [GET] All The Friends
- Add the following code to `friends.py`:
    
    ```python
    @api.route('/api/v1/friends', methods=['GET'])
    def get_friends() -> flask.Response:
        """
        Return a representation of the collection of friend resources.
        
        Returns:
            A flask.Response object.
        """
        friends_list = datastore.friends()
        return flask.jsonify({"friends": friends_list})
    ```
    
- There is a lot going on here. So let's take it line by line.
    - The `@api.route()` is a **decorator**.  Decorators are used in Python 
    programs to dynamically modify an existing function, adding additional
    processing before or after the original function.
    
        > ![Extra Info](../images/reminder.png) Decorators are pretty 
        > advanced so we won't really go into them 
        > during this class. But, feel free to ask if you really want to know ;)
        
    - The `route` decorator connects your function to a
    URL and one or more HTTP methods.  Whenever the specified URL is called
    on your API with one of the specified methods, your function will be called.
        - In this case, it is connecting incoming requests to 
        `http://127.0.0.1:5000/api/v1/friends` using the `GET` to this function. 
        
    - You're familiar with the function definition statement and the docstring 
    by now, but what is `flask.jsonify` function doing?
        - You might guess from the docstring that it returns a flask.Response
        object - which ultimately becomes the HTTP response from your
        API to the client.
        
        - In particular, it creates a HTTP response object with a JSON payload,
        sets the `content-type` header to `application/json` and sets to the
        status code of the response to `200 OK`.
        
        - You can see from the example that you can pass a dictionary to it,
        which will then become the JSON payload.  In this case, we pass
        a dictionary to it with a single key of _friends_ and the value 
        is the list of friends that we retrieve on the previous line.
        
        > ![Extra Info](../images/reminder.png) You can always use `help`
        > on the method, look it up in PyCharm's inline help, or in the 
        > [Flask](http://flask.pocoo.org/docs/0.10/api/#flask.json.jsonify) 
        > documentation.
    
### There Is No Secret Ingredient: Testing
In order to test your API, you'll continue to need two terminal windows open 
with active SSH sessions in your Vagrant VM - just like we did in exercise 2. 

- In the first terminal session make sure that you've gone to `level-4` and
then executed `cd` into your subdirectory.

- From here, you can execute `python run_server.py`.  This will start the test 
HTTP server that is bundled with Flask and load your API into it. 
The output will look like this if everything worked correctly:

    ```bash
     * Restarting with stat
     * Debugger is active!
     * Debugger pin code: 170-875-347
    ```
    
- In your second terminal window, you can issue `curl` commands to access
various methods of your API.  Test your first method with the following command:

    ```bash
    curl 127.0.0.1:5000/api/v1/friends
    ```
    
    > ![Check It Out](../images/information.png) There will be a lot of `curl`
    > commands that you'll be using in this training level.  Some of them
    > can get quite long. Save yourself some frustration and just copy/paste
    > them from the `curl_tests` file which you can find by going to
    > `level-4` on your Vagrant machine (inside the `dragon-warrior` folder
    > for this training level).
    
  
- You should get the following response:
    
    ```
    {
      "friends": [
        {
          "email": "mike@eikonomega.com",
          "firstName": "Big Fat",
          "id": "BFP",
          "lastName": "Panda",
          "notes": "My bestest friend in all the world.",
          "telephone": "574-213-0726"
        },
        {
          "email": "vdiesel4@supercool.edu",
          "firstName": "Vin",
          "id": "VinDi",
          "lastName": "Diesel",
          "notes": "Really annoying guy.  Will never amount to anything.",
          "telephone": "I-HIT-PEOPLE"
        }
      ]
    }
    ```
    
    > ![Problem Alert](../images/alert.png) Remember that both terminal 
    > sessions need to have active SSH connections to the Vagrant VM 
    > (`vagrant ssh`) for this to work correctly.