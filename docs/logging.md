# Logging

In this section we will have a look how we can do logging in python applications. We will also have a look what we should and and what we should not log. 
Logging is important but extra logging can cause a lot of issue. Issues like latency, extra disk space usage etc. 

For logging in python we use logging module of python. Have a look at the code below

<pre>

import logging

logging.debug('This is a debug')
logging.info('This is an info')
logging.warning('This is a warning')
logging.error('This is an error')
logging.critical('This is a critical')
</pre>

It is very basic to do logging in python.

### Configurations

Below are few of the basic configs that will be useful for you. 

level: Sets the log level
filename: This specifies the file.
filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
format: This is the format of the log message.

Lets use this in our applications

<pre>
import click
import requests
import json
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='app.logs')

@click.command()
@click.option('--username', prompt='Github username',
              help='Github username to get repo details.')

def get_projects(username):
	logging.debug("Contacting github for repos.")
	a = requests.get("https://api.github.com/users/"+username+"/repos")
	logging.debug("Github data received.")
    data = json.loads(a.content)
    return data

if __name__ == '__main__':
	logging.debug("Initilizing application.")
    get_projects()
</pre>

Now when you will run this you can see the logs in app.logs file. Now if you want these logging to be configurable you can simply get these as options like below.

<pre>
import click
import requests
import json
import logging


@click.command()
@click.option('--username', prompt='Github username',
              help='Github username to get repo details.')

@click.option('--log-file', prompt='Log file name,
              help='File to which log', default="app.logs")

@click.option('--log-level', prompt='Log level,
              help='Log level to use., default="warn")

log_levels={
	"warn": logging.WARNING,
	"info": logging.INFO,
	"error": logging.ERROR,
	"debug": logging.DEBUG,
	"critical": logging.CRITICAL
}

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=log-file, level=log_levels[log-level])

def get_projects(username):
	logging.debug("Contacting github for repos.")
	a = requests.get("https://api.github.com/users/"+username+"/repos")
	logging.debug("Github data received.")
    data = json.loads(a.content)
    return data

if __name__ == '__main__':
	logging.debug("Initilizing application.")
    get_projects()
</pre>