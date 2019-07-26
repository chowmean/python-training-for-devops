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


###Variable Rules:
You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

<pre>
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/\<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/\<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
</pre>

types of converters:
1. string
2. int
3. float
4. path
5. uuid


###Unique URLs / Redirection Behavior
The following two rules differ in their use of a trailing slash.
<pre>
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
</pre>

###HTTP Methods
Web applications use different HTTP methods when accessing URLs. You should familiarize yourself with the HTTP methods as you work with Flask. By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
<pre>
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
</pre>

###Rendering Templates:
Flask configures the Jinja2 template engine for you automatically<br>
we can use render_template method to render htmls.

<pre>
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
</pre>

hello.html
<pre>
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  Hello {{name}}
{% else %}
   Hello, World!
{% endif %}
</pre>

###Cookies
reading cookies
<pre>
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
</pre>

storing cookies:
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
###Redirects and Errors
<pre>
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
</pre

<pre>
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
</pre>


###APIs with JSON:
<pre>
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user["name"],
        "theme": user['age']
    }
</pre>

def get_current_user():
    return {'name':'ram', 'age':20}
###Sessions:
<pre>
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

</pre>

####How to generate good secret keys:
A secret key should be as random as possible. Your operating system has ways to generate pretty random data based on a cryptographic random generator. Use the following command to quickly generate a value for Flask.secret_key (or SECRET_KEY):

<pre>
python -c 'import os; print(os.urandom(16))'
</pre>