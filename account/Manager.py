from .Account import Account
import utils


class Manager:

    def __init__(self):
        username = 'User'
        password = '1234abcd'
        hash = utils.derive_key(username.lower() + password)
        enc_key = utils.derive_key(password)
        self.accounts = [Account(username, hash, enc_key)]
        self.active_account = self.accounts[0]
        self.active_account.add_credential('example_username', 'abcdef1234', 'example.com', 'some comment')
        self.active_account.add_credential('Mirlan', 'abcdef1234', 'facebook.com', 'Facebook account credentials')

    def login(self, master_name, master_psw):
        loggedin = False
        hash = utils.derive_key(master_name.lower() + master_psw)
        acc = self.find_account(master_name, hash)
        if acc:
            enc_key = utils.derive_key(master_psw)
            acc.set_key(enc_key)
            self.active_account = acc
            loggedin = True

        return loggedin

    def logout(self):
        self.active_account = None

    def is_logged_in(self):
        return self.active_account is not None

    def get_active_account(self):
        return self.active_account

    def find_account(self, master_name, hash):
        master_name = master_name.lower()
        for acc in self.accounts:
            if acc.master_name.lower() == master_name and acc.hash == hash:
                return acc

    def find_by_name(self, master_name):
        master_name = master_name.lower()
        for acc in self.accounts:
            if acc.master_name.lower() == master_name:
                return True

    def create_account(self, master_name, master_psw, hint):
        acc = self.find_by_name(master_name)
        if acc:
            return False

        hash = utils.derive_key(master_name.lower() + master_psw)
        enc_key = utils.derive_key(master_psw)
        acc = Account(master_name, hash, enc_key, hint=hint)
        self.accounts.append(acc)
        self.active_account = acc
        return True

    def remove_active_account(self):
        active = self.get_active_account()
        self.accounts.remove(active)
        self.logout()


manager = Manager()
