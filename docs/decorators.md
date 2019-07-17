# Decorators
###First-Class Objects
First class objects in a language are handled uniformly throughout.

These are the some properties of first class objects

1. To be named by variables.
2. To be passed as arguments to procedures.
3. To be returned as values of procedures.
4. To be incorporated into data structures

In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:
#####Example 1
<pre>
def say_hello(name):
    return "Hello %s"% name
def be_awesome(name):
    return "Yo %s"% name
def greet_bob(greeter_func):
    return greeter_func("Bob")
</pre>

Here, say_hello() and be_awesome() are regular functions that expect a name given as a string. The greet_bob() function however, expects a function as its argument. We can, for instance, pass it the say_hello() or the be_awesome() function:.

We can execute in python shell

<pre>
>>> greet_bob(say_hello)
'Hello Bob'
>>> greet_bob(be_awesome)
'Yo Bob'
</pre> 

###Inner Functions:
It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:
<pre>
def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the first_child() function")
    def second_child():
        print("Printing from the second_child() function")
    second_child()
    first_child()
</pre>

what happens when you call parent function?

<pre>
>>> parent()
Printing from the parent() function
Printing from the second_child() function
Printing from the first_child() function
</pre> 

Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed.

Furthermore, the inner functions are not defined until the parent function is called. They are locally scoped to parent(): they only exist inside the parent() function as local variables. Try calling first_child(). You should get an error:

<pre>
>>>first_child()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'first_child' is not defined
</pre>

Whenever you call parent(), the inner functions first_child() and second_child() are also called. But because of their local scope, they aren’t available outside of the parent() function.

###Returning Functions From Functions:
Python also allows you to use functions as return values. The following example returns one of the inner functions from the outer parent() function:
<pre>
def parent(num):
    def first_child():
        return "Hi, I am Emma"
    def second_child():
        return "Call me Liam"
    if num == 1:
        return first_child
    else:
        return second_child
</pre>

Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference to the function first_child. In contrast first_child() with parentheses refers to the result of evaluating the function. This can be seen in the following example:

<pre>
>>> first = parent(1)
>>> second = parent(2)

>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>'

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
</pre>

You can now use first and second as if they are regular functions, even though the functions they point to can’t be accessed directly:

<pre>
>>> first()
'Hi, I am Emma'

>>> second()
'Call me Liam'
</pre>

##Simple Decorators:
Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example

Example:
<pre>
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
def say_whee():
    print("Whee!")
say_whee = my_decorator(say_whee)
</pre>

Can you guess what happens when you call say_whee()? Try it:

<pre>
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
</pre>

To understand what’s going on here, look back at the previous examples. We are literally just applying everything you have learned so far.

The so-called decoration happens at the following line:
<pre>
say_whee = my_decorator(say_whee)
</pre>

In effect, the name say_whee now points to the wrapper() inner function. Remember that you return wrapper as a function when you call my_decorator(say_whee):

<pre>
>>> say_whee
<function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>
</pre>

However, wrapper() has a reference to the original say_whee() as func, and calls that function between the two calls to print().

#####Put simply: decorators wrap a function, modifying its behavior.

#####Example:
<pre>
from datetime import datetime
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper
def say_whee():
    print("Whee!")
say_whee = not_during_the_night(say_whee)
</pre>

If you try to call say_whee() after bedtime, nothing will happen:

<pre>
>>> say_whee()
</pre>

###Syntactic Sugar!
The way you decorated say_whee() above is a little heavy. First of all, you end up typing the name say_whee three times.

Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:

####Example:
<pre>
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
</pre>

###Reusing Decorators:
Recall that a decorator is just a regular Python function. All the usual tools for easy reusability are available. Let’s move the decorator to its own module that can be used in many other functions.

<pre>
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
@do_twice
def say_whee():
    print("Whee!")
</pre>

###Decorating Functions With Arguments:
Say that you have a function that accepts some arguments. Can you still decorate it? Let’s try:


Example:
<pre>
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def greet(name):
    print " hello %s"%name

def say_whee():
    print "Whee!"
</pre>

Unfortunately, running this code raises an error:

<pre>
>>> greet("World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
</pre>

The problem is that the inner function wrapper_do_twice() does not take any arguments, but name="World" was passed to it. You could fix this by letting wrapper_do_twice() accept one argument, but then it would not work for the say_whee() function you created earlier.

The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an arbitrary number of positional and keyword arguments. Rewrite decorators.py as follows:

<pre>
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
@do_twice
def greet(name):
    print " hello %s"%name
def say_whee():
    print "Whee!"
</pre>

Now call functions 

<pre>
>>> say_whee()
Whee!
Whee!
>>> greet("World")
Hello World
Hello World
</pre>

###Returning Values From Decorated Functions:
What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you decorate a simple function as follows:
<pre>
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
    
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return "Hi %s"%name
</pre>

Call function

<pre>
>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
None
</pre>

Oops, your decorator ate the return value from the function.
modify your wrapper to return something 

<pre>
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
</pre>

###Real world use cases:

1. Timing functions
2. Registering functions
3. checking for authentication


###Examples:
<pre>
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
</pre>
 

