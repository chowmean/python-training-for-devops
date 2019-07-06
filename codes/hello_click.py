import click
import requests
import json
import logging

loglevels={
    "warn": logging.WARNING,
    "info": logging.INFO,
    "error": logging.ERROR,
    "debug": logging.DEBUG,
    "critical": logging.CRITICAL,
}
@click.command()
@click.option('--username', prompt='Github username', help='Github username to get repo details.')
@click.option('--log_file', prompt='Log file name', help='File to which log', default='app.logs')
@click.option('--log_level', prompt='Log level', help='Log level to use', default='warn')
#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename=log-file, level=loglevels[log_level])

def get_projects(username):
    logging.debug("Contacting github for repos.")
    a = requests.get("https://api.github.com/users/"+username+"/repos")
    logging.debug("Github data received.")
    data = json.loads(a.content)
    return data

if __name__ == '__main__':
    logging.debug("Initilizing application.")
    get_projects()
