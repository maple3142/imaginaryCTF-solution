#!/usr/bin/env python3.9

from Crypto.Util.number import *
from hidden import flag

p = getPrime(1024)
q = p

e = 65537
n = p*q

m = bytes_to_long(flag)

c = pow(m, e, n)

print(f'{n = }')
print(f'{c = }')

