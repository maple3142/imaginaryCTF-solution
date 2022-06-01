#!/usr/bin/env python3

from struct import pack, unpack
from hashlib import sha256
from hmac import new
from base64 import b64encode, b64decode

from secret import key

def sign(data):
    size = pack(">H", len(data))
    digest = new(key, data, sha256).digest()
    return b64encode(size + digest + data)

def get_verified_data(data):
    data = b64decode(data)
    if len(data) < 2:
        return None

    size = unpack(">H", data[0:2])[0]
    if len(data) < 2 + 32 + size:
        return None

    provided_hmac = data[2:34]
    expected_hmac = new(key, data[34:34+size], sha256).digest()
    if provided_hmac != expected_hmac:
        return None

    return data[34:]
