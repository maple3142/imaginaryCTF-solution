from pwn import process

# context.log_level = 'debug'
p = 115792089237316195423570985008687907853269984665640564039457584007913129870127
g = 5

io = process(["python", "oracle.py"])
# io = remote("031337.xyz", 42046)


def get_sig(c):
    io.sendlineafter(b"c = ", str(c).encode())
    io.recvuntil(b"t = ")
    t = int(io.recvlineS())
    io.recvuntil(b"s = ")
    s = int(io.recvlineS())
    return t, s

t1, s1 = get_sig(1)
t2, s2 = get_sig(1)
t3, s3 = get_sig(1)
t4, s4 = get_sig(4)
P.<x,a,b,r1,r2,r3,r4>=GF((p-1)//2)[]  # assuming x < (p-1)/2
I=P.ideal([
    r1*a+b-r2,
    r2*a+b-r3,
    r4*a+b-r4,
    s1-(r1+x),
    s2-(r2+x),
    s3-(r3+x),
    s4-(r4+4*x)
])
assert I.dimension() == 0
x = ZZ(I.variety()[0][x])
print(x)

r = 48763
t = pow(g, r, p)
io.sendlineafter(b"t = ", str(t).encode())
io.recvuntil(b"c = ")
c = int(io.recvlineS())
s = (r + c * x) % (p - 1)
io.sendlineafter(b"s = ", str(s).encode())
print(io.recvallS())
# ictf{w34k_n0nc3_gEn3r4t1on_smh}
