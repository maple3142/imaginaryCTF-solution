#!/usr/bin/env python3

from Crypto.Util.number import *
from random import seed, getrandbits

m = bytes_to_long(open('flag.txt', 'rb').read())
print("What's your name?\n>>> ", end='')
name = open(0, 'rb').readline().strip()
seed(bytes_to_long(name))
e = 2*getrandbits(32)+1
p = getPrime(512)
q = getPrime(512)
n = p*q
c = pow(m, e, n)
print(f"Here's your flag, {''.join(chr(i) for i in name)}!")
print(f'{n = }')
print(f'{e = }')
print(f'{c = }')
