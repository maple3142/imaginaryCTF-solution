#!/usr/bin/env python3

from base64 import b64encode
from flag import flag
from string import ascii_letters, digits
from hashlib import sha1
from random import choice
from os import system

password = ''.join(choice(ascii_letters+digits) for i in range(80))
fname = b64encode(sha1(password.encode()).digest()).decode()

with open(fname, 'w') as f:
    f.write(flag)

print(password)
print(fname)

system(f'7z a chall.zip {fname} -mem=AES256 -p{password}')


