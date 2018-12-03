from prompt_toolkit import PromptSession
from account import manager
import cli


def main():
    session = PromptSession()

    while True:
        try:
            active_user = manager.get_active_account()
            prompt_text = "> "

            if active_user:
                prompt_text = "{}> ".format(active_user.master_name)

            text = session.prompt(prompt_text)

            terminate = cli.handle(text)

            if terminate:
                break

        except KeyboardInterrupt as e:
            continue

        except EOFError:
            cli.handle('close')
            break


if __name__ == '__main__':
    main()
