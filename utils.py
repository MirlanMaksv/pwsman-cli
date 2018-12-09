import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from base64 import b64decode, b64encode


def enc_AES(data, key):
    data = b64encode(data.encode())
    key = key
    iv = b'iv' + key
    cipher = AES.new(key, AES.MODE_EAX, iv)
    ciphertext = cipher.encrypt(data)
    return b64encode(ciphertext).decode()


def dec_AES(ciphertext, key):
    ciphertext = b64decode(ciphertext.encode())
    iv = b'iv' + key
    cipher = AES.new(key, AES.MODE_EAX, iv)
    data = cipher.encrypt(ciphertext)
    return b64decode(data).decode()


def derive_key(password, k_len=32):
    # purposefully prefixed the password
    salt = "salt" + password
    return scrypt(password, salt, k_len, 16384, 32, 1)


def sha256(psw):
    # purposefully prefixed the password
    s = "salt" + psw
    return hashlib.sha256(s.encode()).hexdigest()
