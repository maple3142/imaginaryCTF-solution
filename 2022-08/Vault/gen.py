#!/usr/bin/env python3

from Crypto.Util.number import *
from time import time

from secret import flag, gen_ciphertext

def get_difficulty(duration):
    curr_time = time()
    n = 2
    for i in range(10000):
        n = pow(n, 71, 2**1024-1)
    elapsed = time() - curr_time
    print("10000 exponentiations in", elapsed)
    return int(duration * 10000 / elapsed)

def gen_vault(m, duration, fname="vault.txt"):
    m <<= 32
    m += 1
    while not isPrime(m):
        m += 2
    p = getPrime(256)
    q = getPrime(256)
    n = p*q*(p-1)*(q-1)
    diff = get_difficulty(duration)
    print("Difficulty:", diff)
    curr_time = time()
    c = gen_ciphertext(p, q, n, m, diff)
    print("Ciphertext generated in", time()-curr_time)
    file = open(fname, 'w')
    file.write(f"Please raise c to the 71st power {diff} times mod n to get the flag.\n\n")
    file.write(f"{c = }\n")
    file.write(f"{n = }")
    file.close()

if __name__ == '__main__':
    gen_vault(bytes_to_long(flag),  7*24*60*60)