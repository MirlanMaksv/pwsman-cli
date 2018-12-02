class Account:

    def __init__(self, username, password_hash, credentials):
        self.username = username
        self.password_hash = password_hash
        self.credentials = credentials

    def get(self, name):
        pass

    def create(self, name, url, password, comment=None):
        pass

    def remove(self, name):
        pass

    def update(self, name=None, url=None, password=None, comment=None):
        pass
