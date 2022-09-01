from pwn import *
import re

io = remote("puzzler7.imaginaryctf.org", 4006)
for _ in range(100):
    r = rb"\d+ . \d+ = \?"
    m = re.search(r, io.recvregex(r))
    print(m.group(0)[:-4])
    io.sendlineafter(b">>>", str(eval(m.group(0)[:-4])).encode())
context.log_level = "debug"
print(io.recvall())
# ictf{congrats_you've_conquered_the_blackboard...for_now...}
