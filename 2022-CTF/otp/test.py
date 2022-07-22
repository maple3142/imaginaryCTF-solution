#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes, bytes_to_long
import random
import math
from collections import Counter


def secureRand(bits, seed):
    jumbler = []
    jumbler.extend([2**n for n in range(300)])
    jumbler.extend([3**n for n in range(300)])
    jumbler.extend([4**n for n in range(300)])
    jumbler.extend([5**n for n in range(300)])
    jumbler.extend([6**n for n in range(300)])
    jumbler.extend([7**n for n in range(300)])
    jumbler.extend([8**n for n in range(300)])
    jumbler.extend([9**n for n in range(300)])
    print(f'{len(jumbler) = }')
    print(Counter([int(str(x)[0])<5 for x in jumbler]))
    out = ""
    state = seed % len(jumbler)
    for _ in range(bits):
        print(state)
        if int(str(jumbler[state])[0]) < 5:
            out += "1"
        else:
            out += "0"
        state = int(
            "".join(
                [
                    str(jumbler[random.randint(0, len(jumbler) - 1)])[0]
                    for n in range(len(str(len(jumbler))) - 1)
                ]
            )
        )
    return long_to_bytes(int(out, 2)).rjust(bits // 8, b"\0")


for _ in range(2):
    print(secureRand(8, 123))
