
## Introduction

In this part we will be creating a cli application using a well known framework called Click. 

## What you need to start this?

Basic knowledge of python syntax loops, how to use packages and how to run python program. Knowledge of cli app will be a good addition. 

##  Click package

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

Click adds functionality like help by default which is very useful in case of cli apps. Functionality like below

<pre>
(venv) $chowmean@chowmean-MACH-WX9:$ python hello_click.py help
Usage: hello_click.py [OPTIONS]
Try "hello_click.py --help" for help.

Error: Got unexpected extra argument (help)
(venv) $chowmean@chowmean-MACH-WX9:$ python hello_click.py --help
Usage: hello_click.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --help  Show this message and exit.
(venv) $chowmean@chowmean-MACH-WX9:$ 
</pre>

## Lets code

Create a directory for your project. Then create a requirements.txt file in your directory. After that initialize an empty env for you python project and then run pip install to install the required packages. Here package will be click so put click in your requirements file. All of this is below

<pre>
mkdir project_name
cd project_name && touch requirements.txt
virtualenv venv
source venv/bin/activate
echo "click" >> requirements.txt
pip install -r requirements.txt
</pre>

Our project directory is ready create a file with any name and start writing the code below.

Here we will be creating a very basic cli app which says hello. 

<pre>
import click

@click.command()

def hello():
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello')

if __name__ == '__main__':
    hello()

</pre>

Run this using python filename.py and you will see hello as output. 

### Arguments and options

Lets first distinguish between these two. 

*Options* are the values that you can provide to your program through CLI. 

*Arguments*	 work similarly to options but are positional. They also only support a subset of the features of options due to their syntactical nature. 

Arguements cannot do anything more than options so we will have a look at options in detail

#### Options 

For taking options click provide a very easy options. Have a look at code below

<pre>
import click

@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello( name):
    for x in range():
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
</pre>

Here you can take your name as CLI arguement and then this program will print hello your_name. Run this command to run it.

<pre>
python filename.py youname
</pre>

Now you can divide options in two type required and optional ones. 
For that you only have to pass *required=True* and that option will be mandatory

<pre>
import click

@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.', required=True)
def hello( name):
    for x in range():
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
</pre>

In above code now name is a mandatory option. 

### Prompts

Prompts are a way to take user in input at the run time. These are useful when you want to enter some password and don't want it to be recorded in history command. 

There are two types of prompts here. 
#### Input prompts.

Input prompts are used for taking inputs from users. Look at the example below
<pre>
value = click.prompt('Please enter your nanme', type=string)
</pre>

#### Confirmation prompts.
Confirmation prompts are for confirming if you want to continue. 

<pre>
if click.confirm('Do you want to continue?'):
    click.echo('Well done!')
</pre>

You can give option `abort=True`. If you want to abort on not confirming. 

## Click application to pull repos

Here we will build a very small application to get all the public github repos of any users. 

Lets first plan how we will do this. So there will be only two steps. One where we ask for the username of the user to search repos for and next is getting the repo and printing it. 

For first part we will get username like below


<pre>
import click

@click.command()
@click.option('--username', prompt='Github username',
              help='Github username to get repo details.')

def get_projects(username):
    return username

if __name__ == '__main__':
    get_projects()
</pre>

Here we got the input from user to get the username. Now we have to get the details of its repository. 

For that we need to make an api call to open githib apis. For making http calls in python we use a very famous library called requests. 

Look at the code below to understand how requests library works.

<pre>
import requests
a = requests.get("www.google.com")
print(a.content)
</pre>

As simple as this. It supports all the options that are there in http calls like headers, methods etc. We will use this library to make a call to github api. 


Look at the code below

<pre>
import click
import requests

@click.command()
@click.option('--username', prompt='Github username',
              help='Github username to get repo details.')

def get_projects(username):
	a = requests.get("https://api.github.com/users/"+username+"/repos")
    print(a.content)

if __name__ == '__main__':
    get_projects()

</pre>

You got the list of repository but they have lot more data and they need to be in understood by program as object. Right now they are in json format. For handling json we have a library called json in python

Lets see that..

<pre>
import click
import requests
import json

@click.command()
@click.option('--username', prompt='Github username',
              help='Github username to get repo details.')

def get_projects(username):
	a = requests.get("https://api.github.com/users/"+username+"/repos")
    data = json.loads(a.content)
    for item in data:
    	print item['name']

if __name__ == '__main__':
    get_projects()

</pre>

This will print the names of all the repos 