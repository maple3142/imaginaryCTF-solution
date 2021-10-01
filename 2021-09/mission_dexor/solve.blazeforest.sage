from Crypto.Util.number import *
from pwn import xor

password = b"g1v3fl4g"
ct = bytes.fromhex('bdabad262e769d0406e0bd299850a84f57775854f7811b2235ce800d780683075773')
n = len(ct) * 8
M = Matrix(GF(2), n, n)
def to_vector(x: bytes):
    return vector([int(i) for i in bin(bytes_to_long(x))[2:].zfill(n)])
def from_vector(x: tuple):
    return long_to_bytes(int(''.join(str(i) for i in x), 2))
# Matrix s.t Mv == v xor ROR(v, 1)
for i in range(n):
    M[i, i] = 1
    M[(i + 1) % n, i] = 1
# Recursively solve for all possible solutions to the linear equation
def solve(round_no, x):
    if round_no == 5:
        if b'ictf' in x:
            print(x)
        return
    x = xor(x, password)
    x = M \ to_vector(x)
    # Do for all possible solutions
    solve(round_no + 1, from_vector(x))
    for i in M.right_kernel():
        solve(round_no + 1, from_vector(x + i))

solve(0, ct)