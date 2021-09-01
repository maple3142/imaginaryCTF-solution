from base64 import *

s = b"e1JPVH1nM2pSV3AzalkzS3lacEwyVm9cdldvenBVSFx5XGxbM2NtM3dlSFhqVTNyc1hudTNkb1s0WHBEb2RZVC1jbkc7UlM/Pw=="
print(b64decode(s))
r = b64decode(s)[5:]
t = bytes(x - 2 for x in r)
print(t)
print(b64decode(t))
ct = b64decode(t)[5:]

for i in range(256):
    k = bytes([i]) * 100
    xd = bytes(x ^ y for x, y in zip(ct, k))
    if all(32 <= x <= 127 for x in xd) and xd.endswith(b"??"):
        print(xd)
        xxd = bytes([x - 2 for x in xd])
        print(xxd)
        print(i, b64decode(xxd))
