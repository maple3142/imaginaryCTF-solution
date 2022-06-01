from PIL import Image
import numpy as np

primes = np.array(
    [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
    ]
)


def xor(x, y):
    return bytes([a ^ b for a, b in zip(x, y)])


def tobits(b):
    return "".join([f"{x:08b}" for x in b])


def tobytes(b):
    return bytes([int(b[i : i + 8], 2) for i in range(0, len(b), 8)])


img = Image.open("my_image_dl.png")
ar = np.asarray(img)

xx = ar[:64, primes, :]
sx = ""
for i in range(64):
    sx += str((xx[i, i, 0]) & 1) + str((xx[i, i, 2]) & 1)
uid = tobytes(sx).hex()
print(f"ictf{{{uid}}}")
