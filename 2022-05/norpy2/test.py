#!/usr/bin/env python3

from nor import Circuit
import nor
from base64 import b64decode

nor.DEBUG = 1
s = open("intended.nor").read()

circ = Circuit.from_file(s)
print("Running...")
# circ.run(50000)
circ.run(10)
