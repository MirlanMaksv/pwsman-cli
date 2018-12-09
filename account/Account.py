from .Credential import Credential
from utils import enc_AES, dec_AES, sha256


class Account:

    def __init__(self, master_name, hash, enc_key=None, credentials=[], hint=""):
        self.master_name = master_name
        self.hash = hash
        self.enc_key = enc_key
        self.credentials = credentials
        self.hint = hint

    def get_credentials(self):
        return self.credentials

    def decrypted_credentials(self):
        credentials = []
        for c in self.credentials:
            c.password = dec_AES(c.password, self.enc_key)
            credentials.append(c)
        return credentials

    def filter_by(self, value, field=None, credentials=None):
        credentials = credentials if credentials else self.credentials
        filtered = []
        value = value.lower()
        for c in credentials:
            if value in c.__getattribute__(field).lower():
                filtered.append(c)
        return filtered

    def set_key(self, key):
        self.enc_key = key

    def add_credential(self, username=None, password=None, url=None, comment=None):
        encrypted_psw = enc_AES(password, self.enc_key)
        c = Credential(username, encrypted_psw, url, comment=comment)
        self.credentials.append(c)

    def remove_credential(self, index):
        if index < 0 or index >= len(self.credentials):
            return

        return self.credentials.pop(index)
