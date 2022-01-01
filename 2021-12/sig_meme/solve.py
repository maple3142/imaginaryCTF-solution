from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
import base64
import hashlib
import ast
from pwn import *


def encode(x):
    h = hex(x)[2:]
    if len(h) & 1:
        h = "0" + h
    return base64.b64encode(bytes.fromhex(h)).decode("utf-8")


def decode(x):
    return int(bytes.hex(base64.b64decode(x.encode("utf-8"))), 16)


CURVE = secp256k1
PUBKEY = Point(
    0xEE76D532E29172393D72FD06AFCAEC65277806CC44B2E8CA9387D9B797A8A790,
    0x3C1009D0A2F3ECA1479E511E328FEA775455BCC5FE0BDDDBC9E289044278E88F,
    curve=CURVE,
)

# hope two connections are created at the same time
io1 = remote("spclr.ch", 1337)
io2 = remote("spclr.ch", 1337)


def H(t, msg):
    return int(hashlib.sha512(str(t).encode() + msg).hexdigest(), 16)


def recvsig(io, msg):
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"> ", msg)
    io.recvuntil(b"signature:\n")
    x, y, s = map(decode, io.recvlineS().strip().split("."))
    t = Point(x, y, curve=CURVE)
    c = H(t, msg)
    return t, s, c


msg1 = b"Hello, world!"
msg2 = b" Hello, world!"
t1, s1, c1 = recvsig(io1, msg1)
t2, s2, c2 = recvsig(io2, msg2)
d = (s1 - s2) * pow(c1 - c2, -1, CURVE.q)
assert d * CURVE.G == PUBKEY, "unlucky"

# eddsa signing
io1.sendlineafter(b"> ", b"2")
io1.recvuntil(b": ")
msg = ast.literal_eval(io1.recvlineS().strip()).encode()
k = 48763
t = CURVE.G * k
c = H(t, msg)
s = k + d * c
sig = "{}.{}.{}".format(encode(t.x), encode(t.y), encode(s))
io1.sendlineafter(b"> ", sig.encode())
io1.interactive()

# ictf{strip_me_of_my_nonce_reuse_pl34se}
