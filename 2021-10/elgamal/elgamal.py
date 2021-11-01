#!/usr/bin/env python3

from itertools import islice
from math import gcd
from random import randint

class Element:
    def __init__(self, n):
        self.n = Element.reduce(n)

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        return Element(self.n+other.n)

    def __eq__(self, other):
        return self.n == other.n

    def __mul__(self, n):
        ret = Element(1)
        for c in "{:0128b}".format(n):
            ret += ret
            if c == '1':
                ret += self
        return ret

    @staticmethod
    def encode(b):
        ret = 0
        for c in b:
            ret += c
            ret *= 2**8
        return ret//2**8

    @staticmethod
    def reduce(n):
        return n%2**128|1


if __name__ == '__main__':
    gen = Element.encode(b"th3_g3n3ra+0r_p+")
    akey = randint(1, 2**128)|1
    bkey = randint(1, 2**128)|1

    apub = gen*akey
    bpub = gen*bkey

    s = gen*akey*bkey

    flag = open("flag.txt").read()
    flag = flag.replace("ictf{", "").replace("}", "").encode()
    assert len(flag) == 16

    m = Element.encode(flag)
    ct = m*s

    print("gen =", gen)
    print("apub =", apub)
    print("bpub =", bpub)
    print("ct =", ct)
