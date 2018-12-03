from .Credential import Credential


class Account:

    def __init__(self, master_name, master_key, credentials=[], hint=""):
        self.master_name = master_name
        self.master_key = master_key
        self.credentials = credentials
        self.hint = hint

    def get_credentials(self):
        return self.credentials

    def filter_by(self, value, field=None, credentials=None):
        credentials = credentials if credentials else self.credentials
        filtered = []
        value = value.lower()
        for c in credentials:
            if value in c.__getattribute__(field).lower():
                filtered.append(c)
        return filtered

    def add_credential(self, username=None, password=None, url=None, comment=None):
        c = Credential(username, password, url, comment=comment)
        self.credentials.append(c)

    def remove_credential(self, index):
        if index < 0 or index >= len(self.credentials):
            return

        return self.credentials.pop(index)
