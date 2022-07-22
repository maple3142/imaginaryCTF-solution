from pwn import *
from z3 import *

config = [
    [int(a) for a in n.strip()] for n in open("jbox.txt").readlines()
]  # sbox pbox jack in the box
def sha42(s: bytes, rounds=42):
    out = [0] * 21
    for round in range(rounds):
        for c in range(len(s)):
            if config[((c // 21) + round) % len(config)][c % 21] == 1:
                out[(c + round) % 21] ^= s[c]
    return out

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

# io = process(['python', 'hash.py'])
io = remote("hash.chal.imaginaryctf.org", 1337)
for i in range(50):
    io.recvuntil(b'sha42(password) = ')
    h = bytes.fromhex(io.recvlineS().strip())
    password = solve_preimage(h)
    print(i, f'sha42({password.hex()}) = {h.hex()}')
    io.sendlineafter(b'hex(password) = ',password.hex().encode())
io.interactive()
# ictf{pls_d0nt_r0ll_y0ur_0wn_hashes_109b14d1}
