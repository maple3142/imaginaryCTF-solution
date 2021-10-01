from z3 import *

ct = bytes.fromhex(
    "bdabad262e769d0406e0bd299850a84f57775854f7811b2235ce800d780683075773"
)
flag = [BitVec(f"f_{i}", 8) for i in range(len(ct))]
fflag = flag

xor = lambda x, y: [x[z] ^ y[z % len(y)] for z in range(len(x))]


def shift(x):
    t = Concat(*x)
    r = Concat(Extract(0, 0, t), Extract(t.size() - 1, 1, t))
    return [Extract(i + 7, i, r) for i in range(0, t.size(), 8)][::-1]


password = b"g1v3fl4g"
rounds = 5

for u in range(rounds):
    s = shift(flag)
    n = xor(s, password)
    flag = xor(flag, n)

sol = Solver()
for a, b in zip(flag, ct):
    sol.add(a == b)
sol.add(fflag[0] == ord("i"))  # optional, can reduce the number of solutions
while sol.check() == sat:
    m = sol.model()
    ff = bytes([m[x].as_long() for x in fflag])
    print(ff)
    sol.add(Or([a != b for a, b in zip(ff, fflag)]))
