import ast
import numpy as np
from pwn import unbits

q = 2**142 + 217
n = 69

with open("output.txt") as f:
    # f.readline()
    l = f.readline()
    A, b = l.split("] [")
    A = [int(x, 16) for x in ast.literal_eval(A + "]")]
    assert len(A) == n * n
    A = matrix(np.array(A).reshape((n, n)))
    b = [int(x, 16) for x in ast.literal_eval("[" + b)]
    assert len(b) == n

k = 10
A = matrix(A[:k]).T.augment(matrix.identity(n))
print(A.dimensions())
M = A.stack((matrix.identity(k) * q).augment(matrix.zero(k, n)))
print(M.change_ring(Zmod(10)))
load(
    "solver.sage"
)  # https://raw.githubusercontent.com/rkm0959/Inequality_Solving_with_CVP/main/solver.sage

lb = [x - 8 for x in b[:k]] + [0] * n
ub = [x for x in b[:k]] + [1] * n
result, applied_weights, fin = solve(M, lb, ub)
s = vector(ZZ, fin[:n])
print(s)

bits = []
with open("output.txt") as f:
    for l in f:
        A, b = l.split("] [")
        A = [int(x, 16) for x in ast.literal_eval(A + "]")]
        assert len(A) == n * n
        A = matrix(GF(q), np.array(A).reshape((n, n)))
        b = [int(x, 16) for x in ast.literal_eval("[" + b)]
        assert len(b) == n
        e = vector(b) - A * s
        if all([0 <= x < 8 for x in e]):
            bits.append(0)
        else:
            bits.append(1)

print(unbits(bits))
# ictf{l4tt1c3_crypt0_t4k1ng_0v3r_th3_w0rld}
