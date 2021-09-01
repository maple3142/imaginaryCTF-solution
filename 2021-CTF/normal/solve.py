from z3 import *

c1 = bytes.fromhex("44940e8301e14fb33ba0da63cd5d2739ad079d571d9f5b987a1c3db2b60c92a3")
c2 = bytes.fromhex("d208851a855f817d9b3744bd03fdacae61a70c9b953fca57f78e9d2379814c21")


def nor(a, b):
    return [~(x | y) for x, y in zip(a, b)]


flag = [BitVec(f"f_{i}", 8) for i in range(32)]
w1 = nor(flag, c1)
w2 = nor(flag, w1)
w3 = nor(c1, w1)
w4 = nor(w2, w3)
w5 = nor(w4, w4)
w6 = nor(w5, c2)
w7 = nor(w5, w6)
w8 = nor(c2, w6)
out = nor(w7, w8)
sol = Solver()
sol.add(And([x == 0 for x in out]))
assert sol.check() == sat
m = sol.model()
print(bytes([m[x].as_long() for x in flag]))
