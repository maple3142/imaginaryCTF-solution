from pwn import *
import time

# context.log_level = 'debug'

io = remote('puzzler7.imaginaryctf.org', 4001)
io.send(b'\n')
io.recvuntil(b'transmission.\n')
t = time.time()
while True:
    print(io.recvn(1))
    nt = time.time()
    print(nt - t)
    t = nt
io.interactive()
