import click
from cli import cli, echo
from account import manager


@cli.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.option('--password', prompt=True, hide_input=True)
def login(user, password):
    found = manager.login(user, password)
    if not found:
        click.echo('Login or password incorrect')


@cli.command(help='Logout from account')
def logout():
    manager.logout()


@cli.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.password_option()
@click.option('-h', '--hint', type=click.STRING, required=False)
def create(user, password, hint):
    manager.create_account(user, password, hint=hint)


@cli.command(help='Remove account')
@click.option('--password', prompt=True, hide_input=True)
def remove(password):
    acc = manager.get_active_account()
    if acc.master_key != password:
        echo("Passwords do not match, Aborting!")
        return

    click.confirm('Do you want to remove your account?', abort=True)

    # if execution proceeds then user confirmed account removal
    manager.remove_active_account()
