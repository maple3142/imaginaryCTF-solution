from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib, secrets, math, itertools
n = 45546267103257159343575991715120100413155645534562974437144945182596286906116
g = 213415714283782672308383502192890837955
key = secrets.randbits(64)
# can't have a mapsack without a map
pub = list(map(lambda _: pow(g, secrets.randbelow(g), n), range(64)))
print(pub)
# and another map for good measure
P = math.prod(map(lambda i, p: p if (key >> i) & 1 else 1, itertools.count(), pub)) % n
print(P)
with open("flag.txt", "rb") as f:
    flag = f.read().strip()
print(AES.new(hashlib.sha256(key.to_bytes(8, "big")).digest(), AES.MODE_ECB).encrypt(pad(flag, 16)).hex())
