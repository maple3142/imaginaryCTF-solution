#!/usr/local/bin/python

from os import urandom
from secrets import key1, key2, flag
from Crypto.Cipher import AES

def xor(a,b):
    k = b
    while len(b) < len(a):
        b = b + k
    return bytes([x^y for x,y in zip(a,b)])

# generate iv
iv = urandom(16)

# 19 bytes of key :)
assert(len(key1) == 3)
assert(len(key2) + len(key1) == 19)
key1 = key1 + b"\x00"
key1 = key1 * 4

data = input("> ").strip().encode()
if data != b"flag":
    flag = data

# naive padding
flag = flag + b"\x00" * (16 - len(flag)%16)

# do the encryption
flag = AES.new(key1, AES.MODE_CBC, iv=iv).encrypt(flag)
flag = xor(flag, key2)
flag = AES.new(key1, AES.MODE_CBC, iv=iv).encrypt(flag)

print(f"{iv.hex() = }")
print(f"{flag.hex() = }")
