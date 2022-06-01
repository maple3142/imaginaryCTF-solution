#!/usr/bin/env python3

from sympy import factorint, prime
from Crypto.Util.number import bytes_to_long

def strify(n):
    if 0 <= n <= 5:
        return n*'S'+'0'
    d = factorint(n)
    f = []
    for k in d:
        f += [k]*d[k]
    if len(f) > 1:
        return '*'.join('('+strify(i)+')' for i in f)
    return '1+'+strify(n-1)

godel_dict = {
                'S': 1,
                '0': 2,
                '+': 3,
                '*': 4,
                '(': 5,
                ')': 6,
                '1': 7,
             }

def primes():
    n = 1
    while True:
        yield prime(n)
        n += 1

def godelify(s):
    ret = 1
    p = primes()
    for c in s:
        ret *= next(p)**godel_dict[c]
    return ret

if __name__ == '__main__':
    flag = bytes_to_long(open('flag.txt', 'rb').read())
    print(godelify(strify(flag)))
