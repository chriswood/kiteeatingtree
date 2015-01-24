import hashlib

def gen_hash(pw):
    salt = 'M8s2'
    return hashlib.md5(salt + pw).hex_digest()
