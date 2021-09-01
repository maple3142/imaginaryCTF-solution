from gmpy2 import *
from Crypto.Util.number import *

T = 136085
print(bin(T))
flag = 2535320453775772016257932121117911974157173123778528757795027065121941155726429313911545470529920091870489045401698656195217643
l = 420
fnext = (flag >> 1) | ((popcount(flag & T) & 1) << (l - 1))

P = PolynomialRing(GF(2), "x")
x = P.gen()
poly = sum([int(c) * x ^ i for i, c in enumerate(bin(T)[2:][::-1])]) + x ^ l
print(poly)
M = companion_matrix(poly, "bottom")
v = vector(map(int, f"{flag:0420b}"[::-1]))
assert M * v == vector(map(int, f"{fnext:0420b}"[::-1]))
flag = M ^ (-421337) * v
print(long_to_bytes(int("".join(map(str, flag[::-1])), 2))[::-1])
