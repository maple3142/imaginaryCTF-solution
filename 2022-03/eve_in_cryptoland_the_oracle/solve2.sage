from pwn import remote

# context.log_level = 'debug'
p = 115792089237316195423570985008687907853269984665640564039457584007913129870127
g = 5

# io = process(["python", "oracle.py"])
io = remote("031337.xyz", 42046)


def get_sig(c):
    io.sendlineafter(b"c = ", str(c).encode())
    io.recvuntil(b"t = ")
    t = int(io.recvlineS())
    io.recvuntil(b"s = ")
    s = int(io.recvlineS())
    return t, s


# nonce r[n]=a*r[n-1]+b (mod p-1)
# sig t=g^r, s=r+cx
# verify g^s=t*y^c
# c != 0 (mod p-1)

# s1=r1+x
# s2=r2+x
# s3=r3+x
# s2-s1=r2-r1=(a*r1+b)-r1=(a-1)*r1+b=d1
# s3-s2=(a-1)*r2+b=d2
# d2-d1=(a-1)*(r2-r1)=(a-1)*d1

t1, s1 = get_sig(1)
t2, s2 = get_sig(1)
t3, s3 = get_sig(1)
# d1 = (s2 - s1) % (p - 1)
# d2 = (s3 - s2) % (p - 1)

P.<x,a,b,r1,r2,r3>=Zmod(p-1)[]
I=P.ideal([
    r1*a+b-r2,
    r2*a+b-r3,
    s1-(r1+x),
    s2-(r2+x),
    s3-(r3+x)
])
gb = I.groebner_basis()
print(gb)
for f in gb:
    vs = f.variables()
    if len(vs) == 1 and vs[0] == a:
        f = f.univariate_polynomial()
        print(f)
        a=-f[0]/f[1]
        print(a)

qwer = randint(1,p)
t4, s4 = get_sig(qwer)
P.<x,b,r1,r2,r3,r4>=Zmod(p-1)[]
I=P.ideal([
    r1*a+b-r2,
    r2*a+b-r3,
    r3*a+b-r4,
    s1-(r1+x),
    s2-(r2+x),
    s3-(r3+x),
    s4-(r4+qwer*x)
])
gb = I.groebner_basis()
print(gb)
for f in gb:
    vs = f.variables()
    if len(vs) == 1 and vs[0] == b:
        f = f.univariate_polynomial()
        print(f)
        b=-f[0]/f[1]
        print(b)

P.<x,r1,r2,r3,r4>=Zmod(p-1)[]
I=P.ideal([
    r1*a+b-r2,
    r2*a+b-r3,
    r3*a+b-r4,
    s1-(r1+x),
    s2-(r2+x),
    s3-(r3+x),
    s4-(r4+qwer*x)
])
gb = I.groebner_basis()
print(gb)
for f in gb:
    vs = f.variables()
    if len(vs) == 1 and vs[0] == x:
        f = f.univariate_polynomial()
        print(f)
        x=-f[0]/f[1]
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
