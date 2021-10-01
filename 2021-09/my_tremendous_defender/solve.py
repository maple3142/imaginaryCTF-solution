import requests


def find_match(rg: str):
    rg = rg.lstrip("^").rstrip("$")
    s = ""
    for x in rg.split("}"):
        if len(x) == 0:
            continue
        ch = x[1]
        n = int(x[x.index("{") + 1 :])
        s += ch * n
    return s


j = requests.post(
    "http://67.159.89.33:9002/accessToken", json={"password": "peko"}
).json()
print(j["pwReq"])
pwd = find_match(j["pwReq"])
print(pwd)
j = requests.post("http://67.159.89.33:9002/accessToken", json={"password": pwd}).json()
print(j)
pwd_int = int.from_bytes(pwd.encode(), "big")
key = j["signedPassword"] ^ pwd_int
signed_pw = key ^ 1337
j = requests.post(
    "http://67.159.89.33:9002/state", json={"signedPassword": signed_pw}
).json()
print(j)
flag = requests.get(
    f"http://67.159.89.33:{j['port']}/flag", params={"token": j["token"]}
).text
print(flag)
