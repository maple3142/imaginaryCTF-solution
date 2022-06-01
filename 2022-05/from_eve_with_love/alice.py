#!/usr/bin/env python3

from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from random import randint
from hashlib import md5

from signer import sign, get_verified_data
from secret import flag


def die():
    print("Something's not right here...")
    exit()

for fname in ["alice.py", "bob.py", "signer.py"]:
    print('='*80)
    print(f"{fname}:")
    print(open(fname).read())
print('='*80)

g = 2
p = getStrongPrime(512)
a = randint(2, p-1)

gpa_signed = sign(('fromalice '+str(int(g))+' '+str(int(p))+' '+str(pow(g, a, p))).encode()).decode()
print("Please give this to Bob:")
print(gpa_signed)

print()
b_signed = input("What did he say? ")
b_data = get_verified_data(b_signed)
if b_data is None:
    die()

sig, gb = b_data.decode().split(' ')
if sig != "frombob":
    die()
gb = int(gb)

s = pow(gb, a, p)
key = md5(str(s).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
message = sign(cipher.encrypt(pad(flag, 16))).decode()

print("I've encrypted and signed the flag, can you pass it to Bob?")
print(message)
