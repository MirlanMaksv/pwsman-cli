from peewee import SqliteDatabase, Model, CharField, IdentityField, ForeignKeyField, ModelSelect
from utils import dec_AES, enc_AES, derive_key

db = SqliteDatabase('pswman.db')


class BaseModel(Model):
    class Meta:
        database = db


def db_init():
    from .Account import Account
    from .Credential import Credential

    db.connect()
    db.create_tables([Account, Credential])


def db_close():
    db.close()
