from pwn import *
from Crypto.Cipher import AES
import ast
from tqdm import tqdm


def xor(a, b):
    k = b
    while len(b) < len(a):
        b = b + k
    return bytes([x ^ y for x, y in zip(a, b)])


def connect():
    # return process(["python", "mitm_cry.py"])
    return remote("mitm_cry.spclr.ch", 443, ssl=True)


def get_enc(pt: bytes):
    io = connect()
    io.sendlineafter(b"> ", pt)
    io.recvuntil(b"iv.hex() = ")
    iv = bytes.fromhex(ast.literal_eval(io.recvlineS()))
    io.recvuntil(b"flag.hex() = ")
    ct = bytes.fromhex(ast.literal_eval(io.recvlineS()))
    io.close()
    return pt, iv, ct


pt, iv, ct = get_enc(b"peko")
_, flagiv, flagct = get_enc(b"flag")


def all_keys(pt, iv, ct):
    padded_pt = pt + b"\x00" * (16 - len(pt) % 16)
    for a in range(256):
        for b in range(256):
            for c in range(256):
                key1 = bytes([a, b, c, 0]) * 4
                x = AES.new(key1, AES.MODE_CBC, iv=iv).encrypt(padded_pt)
                y = AES.new(key1, AES.MODE_CBC, iv=iv).decrypt(ct)
                key2 = xor(x, y)
                yield key1, key2


pbar = tqdm(total=256 ** 3)
for key1, key2 in all_keys(pt, iv, ct):
    t = AES.new(key1, AES.MODE_CBC, iv=flagiv).decrypt(flagct)
    t = xor(t, key2)
    t = AES.new(key1, AES.MODE_CBC, iv=flagiv).decrypt(t)
    if t[:16].isascii():
        print(t)
    pbar.n += 1
    pbar.update()

# ictf{m33t_in_the_m1ddl3_go_brrrr}
