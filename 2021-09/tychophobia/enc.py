#!/usr/bin/env python3

import random
import hashlib

flag = open("flag.txt", "rb").read()

key = random.randint(0b00000000, 0b11111111)
enc = []

for n in flag:
  enc.append(n^key)
  key = hashlib.md5(bytes([key])).digest()[0]
  if key == 0:
    key += 1

print(bytes(enc))

# output: b'\x1d\x80\x1d\xe0\xa7\x89\x9d\x0f3\xa03`z\x8d\x1b\xbc\xe4\xb7\xcec9\x7f\x8d\x00\xbf\xee\xb7\xc0>js\xafa'
