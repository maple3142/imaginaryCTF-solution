from pwn import *
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from hashlib import md5

context.log_level = "debug"


def connect():
    # aio = process(["python", "alice.py"])
    # bio = process(["python", "bob.py"])
    aio = remote("puzzler7.imaginaryctf.org", 1009)
    bio = remote("puzzler7.imaginaryctf.org", 1010)
    return aio, bio


def dec(b64):
    return b64decode(b64)[34:]


def append(b64, ex):
    return b64encode(b64decode(b64) + ex)


aio, bio = connect()
aio.recvuntil(b"Please give this to Bob:\n")
am = aio.recvlineS().strip()
g, p, ga = map(int, dec(am).split(b" ")[1:])
print(g, p, ga)
bio.sendlineafter(b"What did Alice say?", am.encode())
bio.recvuntil(b"Thanks! Tell her this:\n")
bm = bio.recvlineS().strip()
gb = int(dec(bm).split(b" ")[1])
x = (1 - gb * 10**160) % p
print(x, len(str(x)))
aio.sendlineafter(b"What did he say? ", append(bm, str(x).rjust(160, "0").encode()))
aio.recvuntil(b"I've encrypted and signed the flag, can you pass it to Bob?\n")
key = md5(b"1").digest()
cipher = AES.new(key, AES.MODE_ECB)
print(unpad(cipher.decrypt(dec(aio.recvlineS().strip())), 16))
# ictf{eve_do_you_know_any_good_signing_libraries}
