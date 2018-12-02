from .Account import Account


class Manager:

    def __init__(self):
        self.accounts = [Account("Mars", "1234")]
        self.active_account = self.accounts[0]

    def login(self, name, password):
        loggedin = False
        acc = self.find_account(name, password)
        if acc:
            loggedin = True
            self.active_account = acc

        return loggedin

    def get_active_account(self):
        return self.active_account

    def find_account(self, username, hash):
        for acc in self.accounts:
            if acc.username == username and acc.password_hash == hash:
                return acc

    def create_account(self, name, password, hint):
        acc = Account(name, password, hint=hint)
        self.accounts.append(acc)
        print(self.accounts)

    def remove_account(self, name, password):
        pass


manager = Manager()
