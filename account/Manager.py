from peewee import fn
from .Account import Account
from utils import derive_key


class Manager:

    def __init__(self):
        self.active_account = None

    def login(self, master_name, master_psw):
        loggedin = False
        hash = derive_key(master_name.lower() + master_psw).hex()
        acc = self.find_account(master_name, hash)
        if acc:
            enc_key = derive_key(master_psw)
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
        acc = Account.get_or_none(fn.Lower(Account.master_name) == master_name.lower(), Account.hash == hash)
        return acc

    def find_by_name(self, master_name):
        return Account.get_or_none(fn.Lower(Account.master_name) == master_name.lower())

    def create_account(self, master_name, master_psw, hint):
        acc = self.find_by_name(master_name)
        if acc:
            return False

        hash = derive_key(master_name.lower() + master_psw).hex()
        enc_key = derive_key(master_psw)
        acc = Account(master_name=master_name, hash=hash, hint=hint)
        acc.save()
        acc.set_key(enc_key)

        self.active_account = acc
        return True

    def remove_active_account(self):
        active = self.get_active_account()
        active.delete_instance()
        self.logout()


manager = Manager()
