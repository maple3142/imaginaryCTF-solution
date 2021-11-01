from z3 import *
from Crypto.Util.number import long_to_bytes
import re

inp = [BitVec(f"inp_{i}", 1) for i in range(256)]

vars = globals()


def fn_or(n, a, b, c):
    vars[n] = a | b | c


def fn_and(n, a, b, c):
    vars[n] = a & b & c


with open("3sat.v", "r") as f:
    for _ in range(4):
        f.readline()
    exprs = set()
    while True:
        line = f.readline().strip()
        if not line.endswith(";"):
            break
        line = re.sub(r"\(([^,]+)", '("\\1"', line)
        line = re.sub(r"in", "inp", line)
        exprs.add("fn_" + line[:-1])
    while len(exprs) > 0:
        for x in set(exprs):
            try:
                eval(x)
                exprs.remove(x)
            except:
                pass

sol = Solver()
sol.add(out == 1)
assert sol.check() == sat
m = sol.model()
flag = long_to_bytes(int("".join(str(m[x].as_long()) for x in inp)[::-1], 2))
print(flag)
