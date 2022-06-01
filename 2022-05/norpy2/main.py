#!/usr/bin/env python3

from nor import Circuit
from base64 import b64decode

LOCAL = 0

if LOCAL:
    s = open("x.nor").read()
else:
    s = b64decode(input("Enter the base64 of your .nor file: ")).decode()

circ = Circuit.from_file(s)
print("Running...")
circ.run(50000)

if 'output' not in circ.records:
    print('No output found!')
    exit()

if "TTTF"*10000 in circ.records['output']:
    print(open('flag.txt').read())
else:
    print("The first thousand bits of output were:")
    print(circ.records['output'][:1000])
    print()
    print("Better luck next time!")