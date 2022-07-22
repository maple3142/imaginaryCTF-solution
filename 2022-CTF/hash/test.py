import string
import random
from z3 import *

config = [
    [int(a) for a in n.strip()] for n in open("jbox.txt").readlines()
]  # sbox pbox jack in the box

# secure hashing algorithm 42
def sha42(s: bytes, rounds=42):
    out = [0] * 21
    for round in range(rounds):
        for c in range(len(s)):
            if config[((c // 21) + round) % len(config)][c % 21] == 1:
                out[(c + round) % 21] ^= s[c]
    return out


# random.seed(48763)
password = "".join(
    [random.choice(string.printable) for _ in range(random.randint(15, 20))]
).encode()
print(password)
h = sha42(password)
print(bytes(h).hex())


def solve_preimage(h):
    for l in range(15,21):
        inp = [BitVec(f"inp_{i}", 8) for i in range(l)]
        sol = Solver()
        for x in inp:
            sol.add(And(x != 0, x != 0x10, x < 0x7F))
        for x, y in zip(h, sha42(inp)):
            sol.add(x == y)
        if sol.check() != sat:
            continue
        m = sol.model()
        return bytes([m[x].as_long() for x in inp])


print(bytes(sha42(solve_preimage(h))).hex())
