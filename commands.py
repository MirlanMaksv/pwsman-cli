import click
from account import Manager, Account


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
@click.argument('a', type=click.INT, required=True)
@click.argument('b', type=click.INT, required=True)
def add(a, b):
    click.echo(a + b)


def login(name, password):
    pass


def create():
    pass


def close(_):
    click.echo("GoodBye!")
    return True


@click.command()
@click.pass_context
def help(ctx):
    click.echo(ctx.get_help())


commands = {
    'add': add,
    'login': login,
    'create': create,
    'close': close,
    'help': help,
}
