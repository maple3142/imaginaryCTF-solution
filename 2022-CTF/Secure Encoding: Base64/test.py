from z3 import *
from tqdm import tqdm
from pwn import unbits

with open("out.txt") as f:
    ct = f.read()

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="
eqchr = ct[-1]
charset = charset.replace(eqchr, "")
maps = [BitVec(f"c_{i}", 6) for i in range(len(charset))]


def dec(s):
    ar = []
    for c in s:
        if c == eqchr:
            break
        v = maps[charset.index(c)]
        ar.append(v)
    return ar


sol = Solver()
sol.add(Distinct(*maps))
out = dec(ct)
for i, x in enumerate(tqdm(out)):
    if i % 4 == 0:
        sol.add(Extract(5, 5, x) == 0)
    if i % 4 == 1:
        sol.add(Extract(3, 3, x) == 0)
    if i % 4 == 2:
        sol.add(Extract(1, 1, x) == 0)
print("checking")
print(sol.check())
m = sol.model()
maps = [m[x].as_long() for x in maps]
print(maps)
bits = ""
for c in ct:
    if c == eqchr:
        bits += "000000"
    else:
        bits += f"{maps[charset.index(c)]:06b}"
pt = unbits(bits)
with open("flag.txt", "wb") as f:
    f.write(pt)
assert all(x < 128 for x in pt)
