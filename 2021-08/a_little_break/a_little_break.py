#!/usr/bin/env python3

import sys

def encrypt(msg):
    return bytes((i+15)%94+32 for i in msg)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./a_little_break.py [flag]")
        exit()
    print(encrypt(sys.argv[1].encode()).decode())

# output: :4E7L>J08:7E0E@0J@F0:D0E9:D0i02?@E96C062DJ0492==N

