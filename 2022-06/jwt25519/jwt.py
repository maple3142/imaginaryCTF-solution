#!/usr/bin/env python3

from secret import SECRET_KEY, SECRET_PASSWORD
from base64 import b64encode, b64decode
import hmac
import hashlib
from time import sleep
import json

from ed25519 import signature, publickey, checkvalid

def b64pad(b):
    while len(b) % 4 != 0:
        b += b'='
    return b

class JWT():
    def __init__(self, data):
        self.header = {"alg": "ED25519", "typ": "JWT", "public_key": b64encode(publickey(SECRET_KEY)).decode(), **data}
        self.header_bytes = b64encode(json.dumps(self.header).encode()).replace(b'=', b'')
        if 'username' not in data:
            data['username'] = 'boring_user'
        if data['username'] == 'admin':
            if 'password' not in data or data['password'] != SECRET_PASSWORD:
                data['username'] = "boring_user"
        to_del = []
        for key in data:
            if key != 'username':
                to_del.append(key)
        for key in to_del:
            del data[key]
        self.data = {**data}
        self.data_bytes = b64encode(json.dumps(self.data).encode()).replace(b'=', b'')
        self.signature = signature(self.data_bytes, SECRET_KEY, b64decode(self.header['public_key'].encode()))
        self.signature_bytes = b64encode(self.signature).replace(b'=', b'')

    def validate(self):
        try:
            checkvalid(self.signature, self.data_bytes, b64decode(self.header['public_key'].encode()))
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def from_str(cls, s):
        ret = cls({})
        ret.header_bytes, ret.data_bytes, ret.signature_bytes = s.encode().split(b'.')
        header_bytes = b64pad(ret.header_bytes)
        data_bytes = b64pad(ret.data_bytes)
        signature_bytes = b64pad(ret.signature_bytes)

        ret.header = json.loads(b64decode(header_bytes).decode())
        ret.data = json.loads(b64decode(data_bytes).decode())
        ret.signature = b64decode(signature_bytes)

        return ret

    def __str__(self):
        return b'.'.join([self.header_bytes, self.data_bytes, self.signature_bytes]).decode()
