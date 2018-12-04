import click
from cli import cli
from account import manager


@cli.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.option('--password', prompt=True, hide_input=True)
def login(user, password):
    found = manager.login(user, password)
    if not found:
        click.echo("Login or password incorrect")


@cli.command(help="Logout from account")
def logout():
    manager.logout()


@cli.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.password_option()
@click.option('-h', '--hint', type=click.STRING, required=False)
def create(user, password, hint):
    manager.create_account(user, password, hint=hint)
