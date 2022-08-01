import pickle
from collections import defaultdict

with open("out.pickle", "rb") as f:
    l = pickle.load(f)


st = l[ord("i")]
cur = st
flag = ""
while True:
    flag += chr(next(i for i, x in enumerate(l) if id(x) == id(cur)))
    cur = cur[0]
    if id(cur) == id(st):
        break
print(flag)
# ictf{sphInx_oF-blaCk=qu@rTz~jUdge+my^v0w}
