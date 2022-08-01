#!/usr/bin/env python3

flag = open('flag.txt', 'rb').read()
key = open('/dev/urandom','rb').read(1)[0]
out = []

for c in flag:
    out.append(c^key)
    key = c

print(f'{bytes(out).hex() = }')

# bytes(out).hex() = '970a17121d121d2b28181a19083b2f021d0d03030e1526370d091c2f360f392b1c0d3a340e1c263e070003061711013b32021d173a2b1c090f31351f06072b2b1c0d3a390f1b01072b3c0b09132d33030311'
