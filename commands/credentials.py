import click
from cli import cli, ask
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
def show():
    acc = manager.get_active_account()
    for c in acc.get_credentials():
        print(c.username, c.url, c.password, c.comment)
