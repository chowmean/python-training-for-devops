#Flask
###A Minimal Application
A minimal Flask application looks something like this:

<pre>
from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_user_data(user):
    user_data = db.get(user)
    return user_Data
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
    
    from flask import Flask, render_template, escape
    app = Flask(__name__)   
    
    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % escape(username)
    
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id
    
    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return 'Subpath %s' % subpath

types of converters: <br>
1. string <br>
2. int<br>
3. float<br>
4. path<br>
5. uuid<br>


###Unique URLs / Redirection Behavior
The following two rules differ in their use of a trailing slash.
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/projects/')
    def projects():
        return 'The project page'
    
    @app.route('/about')
    def about():
        return 'The about page'

###Rendering Templates

####Example1:
Flask configures the Jinja2 template engine for you automatically<br>
we can use render_template method to render htmls.


    from flask import Flask, render_template
    app = Flask(__name__)
    
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)


hello.html
    
    <!doctype html>
    <title>Hello from Flask</title>
    {% if name %}
      Hello {{name}}
    {% else %}
       Hello, World!
    {% endif %}


####Example2:
Web applications use different HTTP methods when accessing URLs. You should familiarize yourself with the HTTP methods as you work with Flask. By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
    
    from flask import Flask, render_template
    app = Flask(__name__)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('home'))
        return render_template('login.html', error=error)
    @app.route('/home')
    def home():
        render_template('home.html')
            
login.html

    <html>
      <head>
        <title>Flask Intro - login page</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
      </head>
      <body>
        <div class="container">
          <h1>Please login</h1>
          <br>
          <form action="" method="post">
            <input type="text" placeholder="Username" name="username" value="{{
              request.form.username }}">
             <input type="password" placeholder="Password" name="password" value="{{
              request.form.password }}">
            <input class="btn btn-default" type="submit" value="Login">
          </form>
          {% if error %}
            <p class="error"><strong>Error:</strong> {{ error }}
          {% endif %}
        </div>
      </body>
    </html>
    
home.html

    <html>
      <head>
        <title>Home page</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
      </head>
      <body>
        <div class="container">
          <h1>This is home</h1>
        </div>
      </body>
    </html>




###Redirects:

    from flask import abort, redirect, url_for
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return redirect(url_for('login'))
    
    @app.route('/login')
    def login():
        return 'Hey.. You just landed on log in page'
        
        

###Errors:

    from flask import Flask, redirect, redirect
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return redirect(redirect('login'))
    
    @app.route('/login')
    def login():
        return 'Hey.. You just landed on log in page'
         
    @app.errorhandler(404)
    def page_not_found(error):
        return 'Hey.. you landed on mising page..<br><ul><li>/</li> <li>/login</li> </ul>'
            


###APIs with JSON:

    from flask import Flask, redirect, redirect
    app = Flask(__name__)
    @app.route("/data")
    def data():
        user = get_current_user()
        return {
            "username": user["name"],
            "age": user['age']
        }
    
    def get_current_user():
        return {'name':'ram', 'age':20}

###Cookies

setting cookies:

    from flask import Flas, make_response
    app = Flask(__name__)
    
    @app.route('/set_cookie')
    def set_cookie():
        resp = make_response('hello world')
        username = request.args.get('username')
        resp.set_cookie('username', username)
        return resp
        
reading cookies

    from flask import Flask, request
    app = Flask(__name__)
    
    @app.route('/get_cookie')
    def read_cookie():
        username = request.cookies.get('username')
        return 'hello %'%username

        
###Sessions:
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