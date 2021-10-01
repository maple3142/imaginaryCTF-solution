import secrets
import hashlib, random

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
    x = [SBOX[int(b, 16)] for b in x.hex()]  # Substitution
    random.seed(0x31337)
    random.shuffle(x)  # Permutation
    x = [(a << 4) | b for a, b in zip(x[::2], x[1::2])]
    return xor(rk, bytes(x))  # Network


def E(k, x):
    assert len(x) == BLOCKSIZE
    for rk in key_schedule(k):
        x = round(rk, x)
    return x


def shuffle(x):
    x = [int(b, 16) for b in x.hex()]
    random.seed(0x31337)
    random.shuffle(x)
    x = [(a << 4) | b for a, b in zip(x[::2], x[1::2])]
    return bytes(x)


random.seed(0x31337)
shuffle_tbl = list(range(2 * BLOCKSIZE))
random.shuffle(shuffle_tbl)
inv_shuffle_tbl = [shuffle_tbl.index(i) for i in range(2 * BLOCKSIZE)]


def inv_shuffle(x):
    x = [int(b, 16) for b in x.hex()]
    x = [x[inv_shuffle_tbl[i]] for i in range(len(x))]
    x = [(a << 4) | b for a, b in zip(x[::2], x[1::2])]
    return bytes(x)


def inv_shuffle_x(x):
    for _ in range(ROUNDS):
        x = inv_shuffle(x)
    return x


INV_SBOX = [SBOX.index(i) for i in range(16)]


def sub(x):
    x = [SBOX[int(b, 16)] for b in x.hex()]
    x = [(a << 4) | b for a, b in zip(x[::2], x[1::2])]
    return bytes(x)


def unsub(x):
    x = [INV_SBOX[int(b, 16)] for b in x.hex()]
    x = [(a << 4) | b for a, b in zip(x[::2], x[1::2])]
    return bytes(x)


def sub_x(x):
    for _ in range(ROUNDS):
        x = sub(x)
    return x


def unsub_x(x):
    for _ in range(ROUNDS):
        x = unsub(x)
    return x


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# SBOX is affine, so SBOX[a ^ b] = SBOX[a] ^ SBOX[b]
# So we can deduce that c = shuffle(sub(m)) ^ key = shuffle(sub(m) ^ key_prime)
# so this should be all same
a = b"a" * BLOCKSIZE
print(xor(sub_x(a), inv_shuffle_x(E(KEY, a))).hex())
a = b"b" * BLOCKSIZE
print(xor(sub_x(a), inv_shuffle_x(E(KEY, a))).hex())
a = b"c" * BLOCKSIZE
print(xor(sub_x(a), inv_shuffle_x(E(KEY, a))).hex())

m1 = bytes.fromhex("3e3a79462ca6fc4999a9335ec2c8d20b5e6cb5050cc9c2dac673aaa797116d97")
c1 = bytes.fromhex("14cf10e2ad98f5d4966b2ba17d6737545acaa6b6343f99a3ed8b2a6f132d9615")
c2 = bytes.fromhex("ae3546b7aacec8a86cd584ce5fd732f41d9737a3982ae2d826c428c59549bfa3")
key = xor(sub_x(m1), inv_shuffle_x(c1))
print(unsub_x(xor(key, inv_shuffle_x(c2))))
