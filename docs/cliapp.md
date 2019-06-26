
## Introduction

In this part we will be creating a cli application using a well known framework called Click. 

## What you need to start this?

Basic knowledge of python syntax loops, how to use packages and how to run python program. Knowledge of cli app will be a good addition. 

### Click package

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

### Lets code

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

#### Taking arguement in CLI

For taking arguement click provide a very easy options. Have a look at code below

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