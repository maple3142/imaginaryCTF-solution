import secrets
import hashlib, random

with open("flag.txt", "rb") as f:
    flag = f.read().strip()
    assert flag[:5] == b"ictf{"
    flag = flag[5:]
    assert flag[-1] == b"}"[0]
    flag = flag[:-1]

ROUNDS = 42
BLOCKSIZE = 32
KEY = secrets.token_bytes(BLOCKSIZE)
INPUT = secrets.token_bytes(BLOCKSIZE)
SBOX = [0, 2, 9, 11, 10, 8, 3, 1, 7, 5, 14, 12, 13, 15, 4, 6]

def xor(a, b):
    assert len(a) == len(b)
    return bytes(x ^ y for x, y in zip(a, b))

def key_schedule(k):
    assert len(k) == BLOCKSIZE
    return [hashlib.sha256(k + bytes([i])).digest() for i in range(ROUNDS)]

def round(rk, x):
    x = ([SBOX[int(b, 16)] for b in x.hex()])   # Substitution
    random.seed(0x31337)
    random.shuffle(x)                           # Permutation
    x = [(a<<4) | b for a, b in zip(x[::2], x[1::2])]
    return xor(rk, bytes(x))                    # Network

def E(k, x):
    assert len(x) == BLOCKSIZE
    for rk in key_schedule(k):
        x = round(rk, x)
    return x

if __name__ == "__main__":
    with open("output.txt", "w") as f:
        f.write(f"{INPUT.hex() = }\n")
        f.write(f"{E(KEY, INPUT).hex() = }\n")
        f.write(f"{E(KEY, flag).hex() = }\n")
