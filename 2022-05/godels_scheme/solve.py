from sympy import prime
from Crypto.Util.number import long_to_bytes


def primes():
    n = 1
    while True:
        yield prime(n)
        n += 1


enc = int(open("output.txt").read())


def power(n, p):
    i = 0
    while n % p == 0:
        n //= p
        i += 1
    return i, n


godel_dict = {
    "S": 1,
    "0": 2,
    "+": 3,
    "*": 4,
    "(": 5,
    ")": 6,
    "1": 7,
}
inv_dict = {v: k for k, v in godel_dict.items()}

s = ""
for p in primes():
    e, enc = power(enc, p)
    if e in inv_dict:
        s += inv_dict[e]
    print(enc.bit_length())
    if enc == 1:
        break
print(s)
x = eval(
    s.replace("SSSSS0", "5")
    .replace("SSSS0", "4")
    .replace("SSS0", "3")
    .replace("SS0", "2")
)
print(long_to_bytes(x))
# ictf{everything_is_d@t@}
