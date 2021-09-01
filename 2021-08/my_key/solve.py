from Crypto.Util.number import *

e = 0x10001
n = 0x99EF62AB
d = pow(e, -1, n - 1)

ar = [
    0x4C8E40C2,
    0x2510C41D,
    0x3F820908,
    0x1D3847D7,
    0x189ACAE5,
    0x8FF94A1,
    0x5D1121A7,
    0x5D83702B,
]
for x in ar:
    m = pow(x, d, n)
    print(long_to_bytes(m)[::-1].decode(), end="")
