# ORM

## What are orm?

A simple answer is that you wrap your tables or stored procedures in classes in your programming language, so that instead of writing SQL statements to interact with your database, you use methods and properties of objects.[stackoverflow]

## SQL Alchemy in flask

<pre>
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


admin = User(username="test1asd",email="aasdadsdadsad")
db.session.add(admin)
db.session.commit()

print(User.query.all())
</pre>

Lets see what is happening above. 
First two line from import flask and sql alchemy

Next we created application and defined app.config for sql alchemy. It has to be this variable name only `app.config['SQLALCHEMY_DATABASE_URI']`. Then we intialized db instance. 

Next we have created User class. 

Then we created an instance of User and added it to the session and then commited it. 

This is how data is saved. 

Next we can query it `using the User.query.all()` .



## Flask Migrations

We will use flask-migrate for keeping track of migrations. It uses alembic behind the scenes for migrations. 

### Installation 

<pre>
pip install flask-migrate
</pre>

### Code

Have a look at the below code

<pre>
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=True)
    def __repr__(self):
        return '<User %r>' % self.username
</pre>

As you can see there are 2 new line. Importing flask_migrate and initializing migrate. Thats it you have to do for now. 

### How to create migration. 

##### Initializing

<pre>flask db init</pre>

It will generate migrations folder.

##### Generating Migration

After making code changes in model. You can run the below command to generate migrtion

<pre>flask db migrate</pre>

Now there will be migrations generated and you can see those in migrations/versions folder.

##### Applying migration

<pre>flask db upgrade</pre>

##### Downgrade Migration

<pre>flask db downgrade version</pre>

These are very basic of how you can keep track of your database migrations. You can read more about it. There are lot of complexities involve when it comes to migration with databases. So read about it properly before using it in production. 