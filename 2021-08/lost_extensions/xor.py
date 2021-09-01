import sys

with open(sys.argv[1], "rb") as f:
    data = f.read()

key = sys.argv[2].encode()


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


sys.stdout.buffer.write(xor(key * len(data), data))
