from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
from secret import flag

tobin = lambda x: bytes("".join(f"{i:08b}" for i in x).encode())
tostr = lambda x: ltb(int(x, 2))
xor = lambda x, y: bytes([x[z]^y[z%len(y)] for z in range(len(x))])
shift = lambda s: s[-1:] + s[:-1]

password = b"g1v3fl4g"
rounds = 5

for u in range(rounds):
    s = tostr(shift(tobin(flag)))
    n = xor(s, password)
    flag = xor(flag, n)
    
with open("output.txt", "w") as f:
    f.write(flag.hex())

# output: bdabad262e769d0406e0bd299850a84f57775854f7811b2235ce800d780683075773