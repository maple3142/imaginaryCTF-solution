from pwn import *
from math import gcd
import ast
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

io = remote("031337.xyz", 42043)
io.recvuntil(b"pow(k, e, n) = ")
ken = int(io.recvlineS().strip())
io.recvuntil(b"cipher.encrypt(pad(flag, 16)).hex() = ")
flagct = bytes.fromhex(ast.literal_eval(io.recvlineS().strip()))


def encrypt(p):
    io.sendline(str(p).encode())
    return int(io.recvlineS().strip())


e2 = encrypt(2)
e4 = encrypt(4)
e8 = encrypt(8)
print(2, e2)
print(4, e4)
print(8, e8)
n = gcd(e2**2 - e4, e2**3 - e8)
print(n)

n = 611117054076991376400980934408083166481
p = 22203158984952133907
q = n // p
e = 10757320957461260575
k = pow(ken, pow(e, -1, (p - 1) * (q - 1)), n)
key = hashlib.sha256(hex(k).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
print(unpad(cipher.decrypt(flagct), 16))
# ictf{f4ct0r1ng_&_d1scr3t3_l0gs}
