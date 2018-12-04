from .Account import Account


class Manager:

    def __init__(self):
        self.accounts = [Account("Master_user", "1234")]
        self.active_account = self.accounts[0]
        self.active_account.add_credential("example_username", "abcdef1234", "example.com", "some comment")
        self.active_account.add_credential("Mirlan", "abcdef1234", "facebook.com", "Facebook account credentials")

    def login(self, master_name, master_key):
        loggedin = False
        acc = self.find_account(master_name, master_key)
        if acc:
            loggedin = True
            self.active_account = acc

        return loggedin

    def logout(self):
        self.active_account = None

    def get_active_account(self):
        return self.active_account

    def find_account(self, master_name, hash):
        for acc in self.accounts:
            if acc.master_name == master_name and acc.master_key == hash:
                return acc

    def create_account(self, master_name, master_key, hint):
        acc = Account(master_name, master_key, hint=hint)
        self.accounts.append(acc)

    def remove_active_account(self):
        active = self.get_active_account()
        self.accounts.remove(active)
        self.logout()


manager = Manager()
