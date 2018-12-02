import click
from account import manager, Account


def handle(text):
    args = text.split()
    res = None

    try:
        res = commands[args[0]](args[1:])

    except KeyError:
        click.echo("Command '{}' is not supported. See 'help' for more information".format(text))

    except SystemExit:
        pass

    return res


@click.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.option('--password', prompt=True, hide_input=True)
def login(user, password):
    found = manager.login(user, password)
    if not found:
        click.echo("Login or password incorrect")


@click.command()
@click.option('-u', '--user', type=click.STRING, required=True)
@click.password_option()
@click.option('-h', '--hint', type=click.STRING, required=False)
def create(user, password, hint):
    manager.create_account(user, password, hint=hint)


@click.command()
def credential():
    username = click.prompt("Enter username ")
    password = click.prompt("Enter password ")
    url = click.prompt("Enter url ")
    comment = click.prompt("[Optional] Enter comment ", default="", show_default=False)

    manager.active_account.create_credential()


def close(_):
    click.echo("GoodBye!")
    return True


@click.command()
@click.pass_context
def help(ctx):
    click.echo(ctx.get_help())


commands = {
    'login': login,
    'create': create,
    'close': close,
    'help': help,
    'credential': credential,
}
