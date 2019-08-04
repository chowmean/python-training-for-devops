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