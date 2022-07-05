from pwn import remote
import time

countdownStartTime = 1655500713
l = 0
r = 100000000
while l + 1 != r:
    m = (l + r) // 2
    print(l, r)
    tl = m - (round(time.time()) - countdownStartTime)
    io = remote("155.248.203.119", 42013)
    io.sendlineafter(b"countdown?: ", str(tl).encode())
    s = io.recvlineS().strip()
    print(m, tl, s)
    if "What kind" in s:
        # tl>actual implies m>countdownLength
        l = m
    else:
        r = m
# ictf{n1c3_gu3ss1ng_3fa376}
