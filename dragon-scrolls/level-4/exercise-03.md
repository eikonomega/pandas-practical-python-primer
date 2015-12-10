[Previous](exercise-02.md) |  [Next](exercise-04.md)
## Exercise 3: Storing & Importing Friendship Information
[Code Files](../../training/level-4-creating-web-services/bfp-reference/exercise_02)

No API is really useful without data.  After all, it is data that people and
machines retrieve, create, update, and delete via an API.

We need a place to keep our data.  Later on, we'll use a database for this.
Right now however, we'll just use another module, called `datastore`.

This will allow us to get going quickly, but also has a downside.  All
updates to our program data will only live in memory.  Whenever we restart
the API, the data will be reset to whatever is defined in the `datastore`
module.

### There Is No Secret Ingredient: A Place for Our Data
- Create a new module in your `friends_api` package called `datastore.py`.
- Add the following `list` object to the file.  This will be your initial 
set of friends.  Congratulations, you've got me and Vin Diesel:
    
    ```python
    _friends = [
        {
            "id": "BFP",
            "firstName": "Big Fat",
            "lastName": "Panda",
            "telephone": "574-213-0726",
            "email": "mike@eikonomega.com",
            "notes": "My bestest friend in all the world."
        },
        {
            "id": "VinDi",
            "firstName": "Vin",
            "lastName": "Diesel",
            "telephone": "I-HIT-PEOPLE",
            "email": "vdiesel4@supercool.edu",
            "notes": "Really annoying guy.  Will never amount to anything."
        }
    ]
    ```
        
    - Notice that each element of our list is a dictionary.  This is 
    completely valid.  Remember that lists can hold any time of object 
    as it's elements.
    
    - Also notice the how we've named the list: _friends.  The underscore
    in front of the variable name is a PEP8 convention indicating that
    the variable is intended to be private/internal. In other words, it tells
    other Python programmers that they should access it directly.
    
    > ![New Information](../images/information.png) Remember that the
    > leading underscore is just a convention.  It does not have programmatic
    > effect in the language.  In other words, people are still free to access
    > `_friends` directly if they choose to, but if they're Pythonistas they
    > won't because they'll respect your intentions (or really know what
    > they are doing).
    
- Since we don't want people to directly access the data structure that holds
the information on our friends, let's create a function that will return
the basic list:

    ```python
    def friends() -> list:
        """
        Provide a list of friends.
        
        Returns:
            A `list` containing dictionaries for each friend. 
        """
        return _friends
    
    ```
    
    - As you can see there is almost nothing to this function - at least
    for now.  It's current value is providing a public interface to the
    underlying data structure _and_ giving us the ability to change
    the underlying structure later without have to change the way other 
    modules will interact with the data.
        
- Now let's make sure that we can access information about our friends
from other modules of our `friends_api` package.  
    
    - Update `friends.py` to import the `datastore` module:
    
    ```python
    import flask
    
    from friends_api import datastore
    
    
    api = flask.Flask(__name__)
    ...
    ```

    - Drop to the command line and run `python -i -m friends_api.friends` and 
    see if you can access `datastore.friends()`.  
    
        > ![New Information](../images/information.png) Up to this point in 
        > your training, you've never seen the `-m` flag used before.  You have
        > to use it when executing a package module as a script (like we are doing
        > here).  Otherwise, the `import` statements that refer to other package 
        > modules will break.  
        
    - If you can't, something isn't quite right. Go back and review the steps
    up to this point until it works for you.
    
| [Next Exercise](exercise-04.md)
