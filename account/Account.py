from peewee import CharField
from .db import BaseModel
from utils import dec_AES, enc_AES


class Account(BaseModel):
    master_name = CharField(unique=True)
    hash = CharField()
    hint = CharField()

    def get_credentials(self):
        return list(self.credentials)

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
            if value in getattr(c, field):
                filtered.append(c)
        return filtered

    def set_key(self, key):
        self.enc_key = key

    def add_credential(self, username="", password="", url="", comment=""):
        if not self.enc_key:
            raise Exception("set encryption key")

        encrypted_psw = enc_AES(password, self.enc_key)
        q = Credential.insert(account=self, username=username, password=encrypted_psw, url=url, comment=comment)
        q.execute()

    def remove_credential(self, index):
        return self.get_credentials()[index].delete_instance()


from .Credential import Credential
