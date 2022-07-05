from z3 import *


hash = bytes.fromhex(
    "33383133666562663933303865343663626466616264386261383930613764646562376564663832393062396464663166616537613335633639313930643763"
)
leak = bytes.fromhex("540d54190d")
leak2 = bytes.fromhex("1a0b071541010d")


def solve():
    KL = 6 + 9
    key = [BitVec(f"k_{i}", 8) for i in range(KL)]
    sol = Solver()
    ictf = b"ictf{"
    sol.add(And([key[i] == ictf[i] for i in range(len(ictf))]))
    for x in key:
        sol.add(And(0x20 <= x, x <= 0x7E))
    out = []
    for i in range(len(hash)):
        out.append(hash[i] ^ key[i % KL])
    for i in range(len(leak)):
        sol.add(out[i + 41] == leak[i])
    sol.add(out[47] == 0x45)
    for i in range(len(leak2)):
        sol.add(out[i + 49] == leak2[i])
    if sol.check() == sat:
        m = sol.model()
        key = [m[k].as_long() for k in key]
        print(bytes(key))


solve()
