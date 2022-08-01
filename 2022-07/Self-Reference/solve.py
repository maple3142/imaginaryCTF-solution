import pickle
from collections import defaultdict

with open("out.pickle", "rb") as f:
    l = pickle.load(f)


nxt = {}
dt = {}
for i, x in enumerate(l):
    nxt[id(x)] = id(x[0])
    dt[id(x)] = chr(i)

st = next(k for k, v in dt.items() if v == "i")
cur = st
flag = ""
while True:
    flag += dt[cur]
    cur = nxt[cur]
    if cur == st:
        break

print(flag)
# ictf{sphInx_oF-blaCk=qu@rTz~jUdge+my^v0w}
