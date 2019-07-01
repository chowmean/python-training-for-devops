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

