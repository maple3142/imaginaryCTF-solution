from itertools import product

# fmt: off
index_ar = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
target_ar = [6, 10, 27, 13, 5, 7, 29, 3, 23, 5, 15, 31, 10, 12, 4, 14, 25, 7, 3, 3, 4, 12, 26, 8, 4, 12, 31, 31, 24, 4, 6, 26, 8, 4, 2, 16, 4, 12, 4, 2, 18, 20, 31, 7, 28, 30, 6, 6, 4, 2, 28, 5, 27, 12, 5]
# fmt: on


def to_seq(n):
    ar = [0] * 5
    for i in range(5):
        ar[i] = n % 28
        n += 0xC0FFEE  # the combined value are modified through signal handler...
        n //= 28
    return ar


# test
a, b, c = b"ict"
cb = a | (b << 8) | (c << 16)
print(cb, to_seq(cb))
for x in to_seq(cb):
    print(index_ar[x])
print()


# build inverse map
imap = {}
for a, b, c in product(range(256), repeat=3):
    seq = to_seq(a | (b << 8) | (c << 16))
    imap[tuple(seq)] = bytes([a, b, c])


# solution
untempered = [index_ar.index(x) for x in target_ar]
for i in range(0, len(untempered), 5):
    seq = untempered[i : i + 5]
    print(imap[tuple(seq)].decode(), end="")


# ictf{wh4t_th3_s1gnal_is_go1ng_0n}
