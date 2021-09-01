from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

r = process(argv=["tmp"], executable="./yoda")
r.sendline(b'ictf')
r.interactive()
