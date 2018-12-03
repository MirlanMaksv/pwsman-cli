import click
from cli import cli, ask, number_validator
from account import manager
from keys import *


@cli.group()
def cred():
    pass


@cred.command()
def add():
    questions = {
        K_USERNAME: {K_QUESTION: "Your username : "},
        K_PASSWORD: {K_QUESTION: "Your password : ", K_CONFIG: {'is_password': True}},
        K_URL: {K_QUESTION: "Your url : "},
        K_COMMENT: {K_QUESTION: "[Optional] Comment : ", K_CONFIG: {'default': ""}}
    }
    answers = ask(questions)

    acc = manager.get_active_account()
    acc.add_credential(**answers)


@cred.command('list')
def _list():
    show()


@cred.command('remove')
def remove():
    show()
    question = {'index': {K_QUESTION: 'Enter credential number to remove : ',
                          K_CONFIG: {'validator': number_validator}}}
    answer = ask(question)
    index = int(answer['index']) - 1

    acc = manager.get_active_account()
    cred = acc.remove_credential(index)
    click.echo("Removed {username} {url}".format(username=cred.username, url=cred.url))


def show():
    acc = manager.get_active_account()
    for i, c in enumerate(acc.get_credentials()):
        print("{})".format(i+1), c.username, c.url, c.password, c.comment)
