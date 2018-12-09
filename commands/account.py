import click
from cli import cli, echo, has_access
from account import manager


@cli.command(help='Login to your account')
@click.option('--user', prompt=True, required=True)
@click.option('--password', prompt=True, required=True, hide_input=True)
def login(user, password):
    found = manager.login(user, password)
    if not found:
        click.echo('Login or password incorrect')


@cli.command(help='Create a new account')
@click.option('--user', prompt=True, required=True)
@click.password_option()
@click.option('--hint', prompt=True, default="")
def create(user, password, hint):
    created = manager.create_account(user, password, hint=hint)
    if not created:
        echo('Something went wrong ...')


@cli.command(help='Logout from the account')
def logout():
    if not has_access():
        return

    manager.logout()


@cli.command(help='Remove the account')
@click.option('--password', prompt=True, hide_input=True)
def remove(password):
    if not has_access():
        return

    acc = manager.get_active_account()
    if acc.master_key != password:
        echo('Passwords do not match, Aborting!')
        return

    click.confirm('Do you want to remove your account?', abort=True)

    # if execution proceeds then user confirmed account removal
    manager.remove_active_account()
