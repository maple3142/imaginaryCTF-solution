from Crypto.Util.number import getPrime, bytes_to_long, getRandomRange
from math import prod, gcd

N = prod(getPrime(32) for _ in range(32))
g = 0
while gcd(g, N**2) != 1:
    g = getRandomRange(2, N**2)

with open("flag.txt", "rb") as f:
    flag = bytes_to_long(f.read().strip())
assert flag < N

r = 0
while gcd(r, N) != 1:
    r = getRandomRange(2, N)

c = (pow(g, flag, N**2) * pow(r, N, N**2)) % (N**2)

print(f"{N = }")
print(f"{g = }")
print(f"{c = }")
