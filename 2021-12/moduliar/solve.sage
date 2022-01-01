from pwn import *

io = remote("chal.imaginaryctf.org", 42043)
io.recvuntil(b"p = ")
p = int(io.recvline())
io.recvuntil(b"a = ")
a = int(io.recvline())
io.recvuntil(b"b = ")
b = int(io.recvline())
io.recvuntil(b"a^x = ")
ax = int(io.recvline())
F = GF(p)
a = F(a)
b = F(b)
ax = F(ax)
io.sendlineafter(b"a + b = ", str(a + b).encode())
io.sendlineafter(b"a - b = ", str(a - b).encode())
io.sendlineafter(b"a * b = ", str(a * b).encode())
io.sendlineafter(b"a / b = ", str(a / b).encode())
io.sendlineafter(b"a ^ b = ", str(a ^ b).encode())
io.sendlineafter(b"x = ", str(ax.log(a)).encode())

io.recvuntil(b"truth!")
exec(io.recvuntil(b"p =")[:-3])
p = gcd(gcd(r0 * r2 - r1 ^ 2, r1 * r3 - r2 ^ 2), r2 * r4 - r3 ^ 2)
io.sendline(str(p).encode())

io.recvuntil(b"truth!")
exec(io.recvuntil(b"p =")[:-3])
rs = [r0, r1, r2, r3, r4, r5, r6, r7]
dr = [b - a for a, b in zip(rs, rs[1:])]
ddr = [b - a for a, b in zip(dr, dr[1:])]
p = reduce(gcd, ddr)
io.sendline(str(p).encode())


io.recvuntil(b"truth!")
exec(io.recvuntil(b"p =")[:-3])
rs = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]
dr = [b - a for a, b in zip(rs, rs[1:])]
p = gcd(
    gcd(dr[0] * dr[2] - dr[1] ^ 2, dr[1] * dr[3] - dr[2] ^ 2), dr[2] * dr[4] - dr[3] ^ 2
)
io.sendline(str(p).encode())

io.interactive()

# ictf{gCd_15_7h3_r3@l_mvP!}
