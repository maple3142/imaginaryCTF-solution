#!/usr/bin/env python3

from secret import SECRET_KEY
from base64 import b64encode, b64decode
import hmac
import hashlib
from time import sleep
import json

def b64pad(b):
    while len(b) % 4 != 0:
        b += b'='
    return b

class JWT():
    def __init__(self, data):
        self.header = {"alg": "HSMD5", "typ": "JWT"}
        self.header_bytes = b64encode(json.dumps(self.header).encode()).replace(b'=', b'')
        self.data = data
        self.data_bytes = b64encode(json.dumps(self.data).encode()).replace(b'=', b'')
        self.signature = hmac.new(SECRET_KEY, self.header_bytes + b'.' + self.data_bytes, hashlib.md5).digest()
        self.signature_bytes = b64encode(self.signature).replace(b'=', b'')

    def validate(self):
        correct_hash = hmac.new(SECRET_KEY, self.header_bytes + b'.' + self.data_bytes, hashlib.md5).hexdigest()
        print(self.signature.hex())
        print(correct_hash)
        for i in range(len(correct_hash)):
            if correct_hash[i] != self.signature.hex()[i]:
                return False
            sleep(.1)
        return True

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
