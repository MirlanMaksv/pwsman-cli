from account.Account import Account
import base64
import utils

username = 'User'
password = '01234abcde'
hash = utils.derive_key(username.lower() + password)
enc_key = utils.derive_key(password)
acc = Account(username, hash, enc_key)
print(acc.credentials[0].comment, acc.credentials[1].password)
