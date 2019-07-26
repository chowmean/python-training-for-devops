from flask import Flask, escape, url_for, render_template, session, request, flash, jsonify
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def hello_world():
    return jsonify({'name':"sdgshd"}), 201


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page..'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return render_template('hello.html', name=username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/login')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# app.run()
with app.test_request_context():
    print(url_for('about'))
    print(url_for('about'))
    print(url_for('about', next='/'))
    print(url_for('show_user_profile', username='John Doe'))