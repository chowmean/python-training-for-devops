#flask
###A Minimal Application
A minimal Flask application looks something like this:

<pre>
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
</pre>

######So what did that code do?

1. First we imported the Flask class. An instance of this class will be our WSGI application.

2. Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.

3. We then use the route() decorator to tell Flask what URL should trigger our function.

4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.

Just save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

To run the application you can either use the flask command or python’s -m switch with Flask.<br>
Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

<pre>
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
 </pre>
 

Alternatively you can use python -m flask:

<pre>
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
</pre>

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production


###Externally Visible Server:
If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

<pre>
flask run --host=0.0.0.0
</pre>

This tells your operating system to listen on all public IPs.

###what happens when type flask run?

###Debug Mode:
1. server will reload itself on code changes
2. provide you with a helpful debugger

<pre>
export FLASK_ENV=development
flask run
</pre>


