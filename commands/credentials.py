import click
from tabulate import tabulate
from cli import cli, ask, echo, number_validator, has_access
from account.Manager import manager
from keys import *


@cli.group(help='Credentials related commands')
def cred():
    pass


@cred.command(help='Add a new credential')
def add():
    if not has_access():
        return

    questions = {
        K_USERNAME: {K_QUESTION: 'Your username : '},
        K_PASSWORD: {K_QUESTION: 'Your password : ', K_CONFIG: {'is_password': True}},
        K_URL: {K_QUESTION: 'Url : '},
        K_COMMENT: {K_QUESTION: '[Optional] Comment : ', K_CONFIG: {'default': ''}}
    }
    answers = ask(questions)

    acc = manager.get_active_account()
    acc.add_credential(**answers)


@cred.command('list', help='List all credentials')
@click.option('--show-psw', is_flag=True)
def _list(show_psw):
    if not has_access():
        return

    acc = manager.get_active_account()

    credentials = acc.decrypted_credentials() if show_psw else acc.get_credentials()

    show(credentials, show_psw=show_psw)


@cred.command(help='Search for credentials by username and url')
@click.option('--username', help='Search by username')
@click.option('--url', help='Search by url')
@click.option('--show-psw', is_flag=True)
def search(username, url, show_psw):
    if not has_access():
        return

    acc = manager.get_active_account()
    credentials = acc.decrypted_credentials() if show_psw else acc.get_credentials()

    if username:
        credentials = acc.filter_by(username, K_USERNAME, credentials)
    if url:
        credentials = acc.filter_by(url, K_URL, credentials)

    show(credentials, show_psw=show_psw)


@cred.command(help='Remove credential')
def remove():
    if not has_access():
        return

    acc = manager.get_active_account()
    show(acc.get_credentials())

    question = {'index': {K_QUESTION: 'Enter credential number to remove : ',
                          K_CONFIG: {'validator': number_validator}}}
    answer = ask(question)
    index = int(answer['index']) - 1

    cred = acc.get_credentials()[index]
    username = cred.username
    url = cred.url

    acc.remove_credential(index)
    echo('Removed {username} {url}'.format(username=username, url=url))


def show(credentials, fields=[K_USERNAME, K_URL, K_PASSWORD, K_COMMENT], show_psw=False):
    headers = ["#"]
    for field in fields:
        headers.append(field.capitalize())

    data = []
    for i, c in enumerate(credentials):
        row = [i + 1] + get_as_array(c, fields, show_psw)
        data.append(row)

    echo(tabulate(data, headers, tablefmt='psql'))


def get_as_array(obj, fields, show_psw):
    res = []

    for field in fields:
        if field == K_PASSWORD and not show_psw:
            res.append('*' * 8)
        else:
            res.append(getattr(obj, field))

    return res
