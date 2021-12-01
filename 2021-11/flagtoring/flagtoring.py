from secret import get_e
from gmpy2 import next_prime
import random

with open("flag.txt", "rb") as f:
    flag = int.from_bytes(f.read().strip(), "big")

p = next_prime(flag << 2)
q = next_prime(random.randrange(2**p.bit_length()))

n = p * q
e = get_e(p, q, n)

print(f"{n = }")
print(f"{e = }")
print(f"{pow(int.from_bytes(b'Have a message: flagtoring', 'big'), e, n) = }")
