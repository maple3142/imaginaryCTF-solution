from pwn import *

# context.log_level = "debug"

io = remote("puzzler7.imaginaryctf.org", 2500)
io.recvline()
for _ in range(100):
    q = io.recvlineS().strip()
    print(q)
    ans = eval(q)
    io.sendline(str(ans).encode())
io.interactive()
