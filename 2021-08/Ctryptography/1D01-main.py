#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import os
import random

with open("flag.txt", "rb") as f:
	flag = f.read()
key = os.urandom(16)

def encrypt(message):
	n = long_to_bytes(random.choice(key))
	cipher = AES.new(key, AES.MODE_CTR, nonce=n)
	return cipher.encrypt(message).hex()

print(f"Here is the encrypted flag: {encrypt(flag)}")
while True:
	message = input("What would you like me to encrypt? ").encode()
	print(encrypt(message))
