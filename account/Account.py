from .Credential import Credential


class Account:

    def __init__(self, master_name, master_key, credentials=[], hint=""):
        self.master_name = master_name
        self.master_key = master_key
        self.credentials = credentials
        self.hint = hint

    def get_credentials(self):
        return self.credentials

    def get_credential(self, url):
        for c in self.credentials:
            if c.url == url:
                return c

    def add_credential(self, username, password, url, comment=None):
        c = Credential(username, password, url, comment=comment)
        self.credentials.append(c)

    def remove_credential(self, name):
        pass

    def update_credential(self, name=None, url=None, password=None, comment=None):
        pass
