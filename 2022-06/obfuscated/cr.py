#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long as btl

p = getPrime(1024)
q = getPrime(1024)

n = p*q

def obfuscate(a, b, c, n):
	l = []
	r = a*a*b + a*b + (c+a)*(lambda x, y, z: (x**2*y**3+y**3*z)*pow(x, y, 0xdeadbeef))(c, b, a)
	while r > 0:
		l.append(r % n)
		r //= n
	return l

flag = obfuscate(btl(open("flag.txt", "rb").read()), p, q, n)

e = 65537
c = []

for b in flag:
	c.append(pow(b, e, n))
print(f"{c = }\n")
print(f"{e = }\n")
print(f"{n = }\n")