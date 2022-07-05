import requests
from base64 import b64encode
import json
from time import time


def make_jwt(hdr: dict, data: dict, sig: bytes) -> str:
    h = b64encode(json.dumps(hdr).encode()).replace(b"=", b"")
    d = b64encode(json.dumps(data).encode()).replace(b"=", b"")
    s = b64encode(sig).replace(b"=", b"")
    return b".".join([h, d, s]).decode()


def time_jwt(tok):
    start = time()
    requests.get(url + "/flag", cookies={"token": tok})
    t = time() - start
    if t >= 4:
        # too long, some network problem
        return time_jwt(tok)
    return t


def hh2b(h):
    return bytes.fromhex("".join([f"{x:x}" for x in h]))


# url = "http://localhost:2002"
url = "http://puzzler7.imaginaryctf.org:2002"
hdr = {"alg": "HSMD5", "typ": "JWT"}
forge = {"username": "admin", "created": 48763}
known = [12, 14, 0, 13, 15, 14, 8, 14, 11, 9, 6, 5, 13, 5, 9, 3, 6, 0, 11, 1]
# known = [12, 14, 0, 13, 15, 14, 8, 14, 11, 9, 6, 5, 13, 5, 9, 3, 6, 0, 11, 1, 4, 4, 13, 3, 13, 12, 2, 14, 9, 15, 1, 0]
sig = known + [0] * (32 - len(known))

for i in range(len(known), len(sig)):
    print(sig)
    ar = []
    for j in range(16):
        sig[i] = j
        s = hh2b(sig)
        tok = make_jwt(hdr, forge, s)
        # t = sum([time_jwt(j) for _ in range(2)]) / 2
        t = time_jwt(tok)
        print(s.hex(), t)
        ar.append((t, list(sig)))
    sig = max(ar, key=lambda x: x[0])[1]
flag = requests.get(
    url + "/flag", cookies={"token": make_jwt(hdr, forge, hh2b(sig))}
).text
print(flag)
# ictf{side_channel_attacks_are_jwst_the_w0rst}
