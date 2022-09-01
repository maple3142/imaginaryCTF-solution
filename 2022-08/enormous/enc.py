#!/usr/bin/env python3

from Crypto.Util.number import *

m = bytes_to_long(open('flag.txt', 'rb').read())

n = 1
for i in range(5):
    n *= getPrime(2025)

e = 31
c = pow(m, e, n)

print(f'{n = }')
print(f'{c = }')
