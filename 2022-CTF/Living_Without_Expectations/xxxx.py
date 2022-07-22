from sage.all import *
import numpy as np
import secrets

q = 2**142 + 217
n = 69
nseeds = 142


def rand(seed):
    seeds = [(seed >> (3 * i)) & 7 for i in range(nseeds)]
    a = 5
    b = 7
    while True:
        for i in range(nseeds):
            seeds[i] = (a * seeds[i] + b) & 7
            yield seeds[i]


rng = rand(secrets.randbits(3 * nseeds))
s = np.array([secrets.randbits(1) for _ in range(n)])
A = np.array([secrets.randbelow(q) for _ in range(n * n)]).reshape((n, n))
e = np.array([next(rng) for _ in range(n)])
b = (A @ s + e) % q
# b = np.array([secrets.randbelow(q) for _ in range(n)])
print(e, file=sys.stderr)

k = 10
A = matrix(A[:k]).T.augment(matrix.identity(n))
print(A.dimensions())
M = A.stack((matrix.identity(k)*q).augment(matrix.zero(k,n)))
print(M.change_ring(Zmod(10)))
load('solver.sage')

lb = [x-8 for x in b[:k]] + [0]*n
ub = [x for x in b[:k]] + [1]*n
result, applied_weights, fin = solve(M, lb, ub)
print(fin[:n])
