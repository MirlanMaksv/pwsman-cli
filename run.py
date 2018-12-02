from __future__ import unicode_literals
from prompt_toolkit import PromptSession
import click


def main():
    session = PromptSession()

    while True:
        try:
            text = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print('You entered:', text)
        if click.confirm('Do you want to continue?'):
            click.echo('Well done!')
    print('GoodBye!')


if __name__ == '__main__':
    main()
