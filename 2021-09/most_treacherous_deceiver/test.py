from Crypto.Util.number import getPrime
from secrets import randbelow

m = getPrime(128)
a = randbelow(m)
c = randbelow(m)

def next_token(current_token):
    return (a * current_token + c) % m

ar = [randbelow(m)]
for _ in range(10):
    ar.append(next_token(ar[-1]))
s = ar
# fmt: on
t = [b - a for a, b in zip(s, s[1:])]
u = []
for i in range(len(t) - 2):
    u.append(abs(t[i + 2] * t[i] - t[i + 1] ** 2))
reduce(gcd,u)
