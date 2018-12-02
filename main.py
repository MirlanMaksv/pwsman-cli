from prompt_toolkit import PromptSession
from account import manager
import commands


def main():
    session = PromptSession()

    while True:
        try:
            active_user = manager.get_active_account()
            prompt_text = "> "

            if active_user:
                prompt_text = "{}> ".format(active_user.username)

            text = session.prompt(prompt_text)

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
