from pwn import *
from hashlib import sha256

map = {sha256(bytes([x])).hexdigest(): chr(x) for x in range(256)}

io = remote("spclr.ch", 1350)

flagar = ["*"] * 100

while True:
    io.sendlineafter(b">", b"2")
    toks = io.recvlineS().strip().split()
    idx = int(toks[0])
    ch = map[toks[1]]
    flagar[idx] = ch
    print("".join(flagar))

# ictf{m0r3_h4sh3s_4r3_m0r3_s3cur3_r1ght?}
