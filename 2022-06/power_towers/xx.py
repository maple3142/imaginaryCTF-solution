from sage.all import GF, legendre_symbol
from Crypto.Util.number import getPrime, isPrime


while True:
    q = getPrime(64)
    p = 2*2*q+1
    if isPrime(p) and p%3==2 and (p*p)%5==4:
        break
F = GF(p)
print(F(3).multiplicative_order())
print(F(5).multiplicative_order())
