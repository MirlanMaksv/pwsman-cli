from account.Account import Account
import base64
import utils


username = 'User'
password = '01234abcde'
hash = utils.derive_key(username.lower() + password)
enc_key = utils.derive_key(password)

encrypted_psw = utils.enc_AES("12345678", enc_key)
decrypted_psw = utils.dec_AES(encrypted_psw, enc_key)
print("KEY", enc_key.hex())
print(encrypted_psw)
print(decrypted_psw)

print(bytes.fromhex(enc_key.hex()))
