import click

@click.command()

def hello():
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello')

if __name__ == '__main__':
    hello()