[Previous](readme.md) |  [Next](exercise-02.md)
## Exercise 1: Project Skeleton
In this exercise, we'll create our basic project folder structure and
install the Flask package.

You'll notice this setup will be slightly different that previous levels
in that there will be two levels of directories.

The two-level directory structure that we'll employ here is what you'd likely 
find in real world Python projects.  

The outer directory contains readme files, licenses, requirements files, etc.  
Generally things that aren't code. The exception to this are executable scripts 
that will call into your inner code directory.
 
The inner directory, which ofter mimics the name of the outer directory in the
real world is actually a **package** - a group of related Python modules 
that work with each other to comprise an application.

### There Is No Secret Ingredient
- Inside your VM, go to the training folder for this level: `cd level-4`

- Create a `your_github_username` directory to store your work.

- Inside directory create a `requirements.txt` file with the following:

    ```txt
    flask==0.10.1
    ```
    
- Use `pip` to install the `flask` package via the `requirements.txt` file: `pip install -r requirements.txt`

- Create a file called `run_server.py` with this content:

    ```python
    from friends_api.friends import app

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
    ```

    - This is a wrapper that will launch a simple HTTP server that will 
    make our API available for testing at `http://127.0.0.1:5000`.  
    In the real world, you'd probably use `gunicorn` to run your program, 
    but this will work for our purposes.
    
    > ![Info](../images/information.png) If the `import` doesn't make sense 
    that's a good thing!  We haven't created the things yet that it is 
    trying to import.
    
- Finally, inside your directory, create a new Python package called 
`friends_api`.  This is where you will keep the code for your api.
    
    > ![Remember](../images/reminder.png) Remember what makes the difference
    > between a normal directory and a Python package?
    
| [Next Exercise](exercise-02.md)
    



   
