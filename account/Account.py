class Account:

    def __init__(self, username, password_hash, credentials=[], hint=""):
        self.username = username
        self.password_hash = password_hash
        self.credentials = credentials
        self.hint = hint

    def get_credentials(self):
        return self.credentials

    def get_credential(self, url):
        pass

    def create_credential(self, name, password, url, comment=None):
        pass

    def remove_credential(self, name):
        pass

    def update_credential(self, name=None, url=None, password=None, comment=None):
        pass
