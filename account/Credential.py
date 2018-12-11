from peewee import CharField, ForeignKeyField
from .db import BaseModel
from .Account import Account


class Credential(BaseModel):
    account = ForeignKeyField(Account, backref='credentials')
    username = CharField()
    password = CharField()
    url = CharField(null=True)
    comment = CharField(null=True)
