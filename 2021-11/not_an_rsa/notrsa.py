import os
from Crypto.Util.number import bytes_to_long

flag = b"<REDACTED>"
c = []

a = bytes_to_long(os.urandom(1))
b = bytes_to_long(os.urandom(1))

for m in flag:
  c.append(a ^ m)
  a = (a + b) % 256

print(f"{bytes(c) = }")

# bytes(c) = b'\xf2\xa3\x91lT=\r\xed\x9c\x9ahS;\x10\xd8\x99\x85\x7fA\x05\r\xd7\xa8\xb1\x7fW1\xff'
