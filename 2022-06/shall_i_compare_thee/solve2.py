import asyncio
import httpx
from base64 import b64encode
import json
from time import time


def make_jwt(hdr: dict, data: dict, sig: bytes) -> str:
    h = b64encode(json.dumps(hdr).encode()).replace(b"=", b"")
    d = b64encode(json.dumps(data).encode()).replace(b"=", b"")
    s = b64encode(sig).replace(b"=", b"")
    return b".".join([h, d, s]).decode()


async def time_jwt(client, tok):
    start = time()
    await client.get("/flag", cookies={"token": tok})
    return time() - start


def hh2b(h):
    return bytes.fromhex("".join([f"{x:x}" for x in h]))


async def main():
    # url = "http://localhost:2002"
    url = "http://puzzler7.imaginaryctf.org:2002"
    async with httpx.AsyncClient(base_url=url) as client:
        hdr = {"alg": "HSMD5", "typ": "JWT"}
        forge = {"username": "admin", "created": 48763}
        sig = [0] * 32

        for i in range(len(sig)):
            print(sig)
            ar = []
            cors = []
            sigs = []
            for j in range(16):
                sig[i] = j
                s = hh2b(sig)
                tok = make_jwt(hdr, forge, s)
                cors.append(time_jwt(client, tok))
                sigs.append(list(sig))
            ts = await asyncio.gather(*cors)
            ar = list(zip(ts, sigs))
            sig = max(ar, key=lambda x: x[0])[1]
        flag = (await client.get(
            "/flag", cookies={"token": make_jwt(hdr, forge, hh2b(sig))}
        )).text
        print(flag)


asyncio.run(main())
