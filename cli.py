import click
from account import manager, Account
from keys import *


def handle(text):
    args = text.split()
    res = None

    try:
        func = args[0]
        if text == 'help':
            func = 'cli'
            args = ['', '--help']

        res = commands[func](args[1:])

    except KeyError:
        click.echo("Command '{}' is not supported. See 'help' for more information".format(text))

    except SystemExit:
        pass

    return res


@click.group()
def cli():
    """A simple Password Manager command line tool."""


def close(_):
    click.echo("GoodBye!")
    return True


def ask(questions):
    answers = {}
    for key, value in questions.items():
        if value.get(K_CONFIG):
            userinput = prompt(value[K_QUESTION], **value[K_CONFIG])
        else:
            userinput = prompt(value[K_QUESTION])

        answers[key] = userinput

    return answers


from commands.account import login, create
from commands.credentials import cred

commands = {
    'cli': cli,
    'login': login,
    'create': create,
    'close': close,
    'cred': cred,
}
