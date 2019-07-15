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
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='app.logs', level=logging.DEBUG)

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

log_levels={
    "warn": logging.WARNING,
    "info": logging.INFO,
    "error": logging.ERROR,
    "debug": logging.DEBUG,
    "critical": logging.CRITICAL
}



@click.command()
@click.option('--username', prompt='Github username', help='Github username to get repo details.')
@click.option('--logfile', prompt='Log file name', help='File to which log', default="app.logs")
@click.option('--loglevel', prompt='Log level', help='Log level to use.', default="warn")
def get_projects(username, logfile, loglevel):
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=logfile, level=log_levels[loglevel])
    logging.debug("Contacting github for repos.")
    a = requests.get("https://api.github.com/users/"+username+"/repos")
    logging.debug("Github data received.")
    data = json.loads(a.content)
    return data

if __name__ == '__main__':
    get_projects()
</pre>

#Rotating Logs:
Python’s logging module has lots of options. In this article, we will looks at the logging module’s ability to create Rotating Logs. Python supports two types of rotating logs:
1) Rotate logs based on size (RotatingFileHandler)
2) Rotate the logs based on some time interval (TimedRotatingFileHandler)

###The RotatingFileHandler:
   It rotates the logs based on the size of the log file.
   We can specify the size with "maxBytes" parameter.
 
   The handler will close the file and silently open a new one. If you pass in a number for the backupCount parameter, then it will append “.1”, “.2”, etcetera to the end of the log files. Let’s take a look at a simple example:
   <pre>
import logging
import time
 
from logging.handlers import RotatingFileHandler
def create_rotating_log(path):
    """
    Creates a rotating log based on size 
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(path, maxBytes=20, backupCount=5)
    logger.addHandler(handler) 
    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)
 
if \__name__ == "\__main__":
    log_file = "test.log"
    create_rotating_log(log_file)
</pre>

####Understanding above code in steps:
1. we create a log file with a logging level of INFO.
2. Then we set up the handler to rotate the log whenever the log file is 20 bytes in length
3. we create a loop that will create 10 lines in our log file with a sleep in between each call to log.

###The TimedRotatingFileHandler:
The TimedRotatingFileHandler allows the developer to create a rotating log based on how much time has elapsed.
You can set it to rotate the log on the following time conditions:

1. second (s)
2. minute (m)
3. hour (h)
4. day (d)
5. w0-w6 (weekday, 0=Monday)
6. midnight

###Example:
<pre>
import logging
import time
 
from logging.handlers import TimedRotatingFileHandler
 
def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)
    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)
 
if \__name__ == "\__main__":
    log_file = "timed_test.log"
    create_timed_rotating_log(log_file)
</pre>



       