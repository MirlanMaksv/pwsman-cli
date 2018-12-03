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

    def add_credential(self, username=None, password=None, url=None, comment=None):
        c = Credential(username, password, url, comment=comment)
        self.credentials.append(c)

    def remove_credential(self, index):
        if index >= len(self.credentials):
            return

        self.credentials.pop(index)

    def update_credential(self, username=None, password=None, url=None, comment=None):
        pass
