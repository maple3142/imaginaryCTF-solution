from z3 import *
from tqdm import tqdm
import string

with open("out.txt") as f:
    ct = f.read()


badchar = b"`\\|<>/;{}"
badchar = b''
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="
eqchr = ct[-1]
charset = charset.replace(eqchr, "")
maps = [BitVec(f"c_{i}", 6) for i in range(len(charset))]


def dec(s):
    ar = []
    for c in s:
        if c == eqchr:
            v = BitVecVal(0, 6)
        else:
            v = maps[charset.index(c)]
        ar.append(v)
    return ar


def dec2(s):
    ar = []
    for c in s:
        if c == eqchr:
            v = 0
        else:
            v = maps_i[charset.index(c)]
        ar.append(v)
    return ar

sol = Solver()
sol.add(Distinct(*maps))
out = dec(ct[:20000])
bs = []
for a, b, c, d in tqdm(
    [out[i : i + 4] for i in range(0, len(out), 4)][:-1]
):  # drop last chunk because of null bytes problem
    b1 = Extract(11, 4, Concat(a, b))
    b2 = Extract(9, 2, Concat(b, c))
    b3 = Extract(7, 0, Concat(c, d))
    for b in [b1, b2, b3]:
        sol.add(ULE(b, 0x7f))
        # sol.add(Or(And(ULE(0x20, b), ULE(b, 0x7F)), b == 0x0A))
        sol.add(And([b!=x for x in badchar]))
    bs += [b1, b2, b3]
prefix = """The Project Gutenberg eBook of The Picture of Dorian cray, by Oscar Wilde

This eBook is for the\x00\x00se of anyone anywhere in the United States and
most other par\x00\x00 of the\x00\x00orld at no cost and\x00\x00ith almost no\x00\x00estrictions
whatsoever. You may co\x00\x00 it, give it away or re-use it under the\x00"""
for x, y in zip(bs, prefix.encode()):
    if y!=0:
        sol.add(x==y)
it = 1
while True:
    print("checking")
    assert sol.check() == sat
    m = sol.model()
    maps_i = [m[x].as_long() for x in maps]
    print(maps_i)
    out2 = dec2(ct)
    ar = []
    for a, b, c, d in tqdm([out2[i : i + 4] for i in range(0, len(out2), 4)]):
        b1 = (((a << 6) | b) >> 4) & 0xFF
        b2 = (((b << 6) | c) >> 2) & 0xFF
        b3 = (((c << 6) | d) >> 0) & 0xFF
        ar += [b1, b2, b3]
    pt = bytes(ar)
    with open(f"rec/recovered_{it}.txt", "wb") as f:
        f.write(pt)
    it += 1
    sol.add(Or([x != y for x, y in zip(maps, maps_i)]))
    break
