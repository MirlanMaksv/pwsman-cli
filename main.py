from __future__ import unicode_literals
from prompt_toolkit import PromptSession
import commands


def main():
    session = PromptSession()

    while True:
        try:
            text = session.prompt('> ')

            terminate = commands.handle(text)

            if terminate:
                break

        except KeyboardInterrupt as e:
            continue

        except EOFError:
            commands.handle('close')
            break


if __name__ == '__main__':
    main()
