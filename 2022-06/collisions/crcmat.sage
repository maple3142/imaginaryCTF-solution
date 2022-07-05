from zlib import crc32
from tqdm import tqdm


def v2b(v):
    v = v[::-1]
    return bytes([int("".join(map(str, v[i : i + 8])), 2) for i in range(0, len(v), 8)])


def b2v(b):
    v = []
    for x in b:
        v.extend(list(map(int, f"{x:08b}")))
    return v[::-1]


def i2v(i, n):
    return list(map(int, f"{i:0{n}b}"))[::-1]


def v2i(v):
    return int("".join(map(str, v[::-1])), 2)


def crcmat(crc, n, m):
    """
    Recover matrix of crc by black box
    crc: crc function, bytes->int
    n: crc output bits
    m: crc input bits

    crc(x) = Ax+C
    x is n bits
    crc(x) is m bits
    A is m by n matrix
    Assuming bits reversed crc
    """
    C = vector(GF(2), i2v(crc(v2b([0] * m)), n))
    right = [None] * m
    vb = bytearray(b"\x00" * (m // 8))
    for i in tqdm(range(m)):
        vb[(m - i - 1) // 8] |= 1 << (i % 8)
        v = [0] * m
        v[i] = 1
        right[i] = vector(i2v(crc(vb), n)) - C
        vb[(m - i - 1) // 8] = 0
    R = matrix(GF(2), right).T
    A = R
    return A, C


if __name__ == "__main__":
    with open("orig_image.png", "rb") as f:
        image_bytes = f.read()
    A, C = crcmat(crc32, 32, len(image_bytes) * 8 + 32)
    P = PolynomialRing(GF(2), 32, 'x')
    xs = P.gens()
    x = A * vector(list(xs) + b2v(image_bytes)) + C
    M, v = Sequence(x).coefficient_matrix()
    print(vector(v))
    M = M.dense_matrix()
    extra = M[:,:-1].solve_right(-M[:,-1])
    new_bytes = image_bytes + v2b(extra.list())
    print(crc32(new_bytes))
    with open('new_image.png', 'wb') as f:
        f.write(new_bytes)
    # simpler image forging: https://blog.stalkr.net/2011/03/crc-32-forging.html
    # file hosting trick: Discord
