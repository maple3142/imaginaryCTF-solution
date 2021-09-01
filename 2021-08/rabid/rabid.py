from Crypto.Util.number import getPrime, isPrime, bytes_to_long

def nextPrime(x):
    x |= (~x) & 1
    x += 2
    while not isPrime(x):
        x += 2
    return x

p = getPrime(512)
q = nextPrime(p)
r = nextPrime(q)
s = nextPrime(r)
N = p * q * r * s

with open("flag.txt", "rb") as f:
    flag = bytes_to_long(f.read().strip())
assert flag < N

c = pow(flag, 2, N)

print(f"{N = }")
print(f"{c = }")
