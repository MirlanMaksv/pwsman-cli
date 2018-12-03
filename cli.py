from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator
from account import manager, Account
from keys import *
import click


def init():
    from commands.account import login, create
    from commands.credentials import cred

    global commands
    commands = {
        'cli': cli,
        'login': login,
        'create': create,
        'close': close,
        'cred': cred,
    }


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


def is_number(text):
    return text.isdigit()


number_validator = Validator.from_callable(
    is_number,
    error_message='This input contains non-numeric characters',
    move_cursor_to_end=True)
