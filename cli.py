from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator
from functools import update_wrapper
from account import Account
from account.Manager import manager
from account.db import db_init, db_close
from keys import *
import click


def init():
    from commands.account import login, logout, create, remove
    from commands.credentials import cred

    global commands
    commands = {
        'cli': cli,
        'login': login,
        'logout': logout,
        'create': create,
        'remove': remove,
        'close': close,
        'cred': cred,
    }

    db_init()


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
        echo("Command '{}' is not supported. See 'help' for more information".format(text))

    except SystemExit:
        if text == 'close':
            return True


@click.group()
def cli():
    '''A simple Password Manager command line tool.'''


@cli.command(help='Close the shell')
def close():
    echo('GoodBye!')
    db_close()


def echo(*messages):
    message = ''
    for m in messages:
        message += m + ' '

    try:
        click.echo(message)
    except SystemExit:
        pass


def ask(questions):
    answers = {}
    for key, value in questions.items():
        if value.get(K_CONFIG):
            userinput = prompt(value[K_QUESTION], **value[K_CONFIG])
        else:
            userinput = prompt(value[K_QUESTION])

        answers[key] = userinput

    return answers


def has_access():
    if not manager.is_logged_in():
        echo('Login required')
        return False
    return True


def is_number(text):
    return text.isdigit()


number_validator = Validator.from_callable(
    is_number,
    error_message='This input contains non-numeric characters',
    move_cursor_to_end=True)
