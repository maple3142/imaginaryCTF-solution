from pwn import *

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
d1 = (s2 - s1) % (p - 1)
d2 = (s3 - s2) % (p - 1)

if d1 % 2 == 1:
    a = (d2 - d1) * pow(d1, -1, p - 1) % (p - 1) + 1
else:
    print("QAQ")
    exit()

print(f"{a = }")

# s3=r3+x
# s4=r4+x*a
# s4-s3*a=(r4+x*a)-(r3+x)*a=b
t4, s4 = get_sig(a)
b = (s4 - s3 * a) % (p - 1)
print(f"{b = }")

if a % 2 == 1:
    print("QAQ")
    exit()
r2 = (d2 - b) * pow(a - 1, -1, p - 1) % (p - 1)
x = (s2 - r2) % (p - 1)
print(f"{x = }")

r = 48763
t = pow(g, r, p)
io.sendlineafter(b"t = ", str(t).encode())
io.recvuntil(b"c = ")
c = int(io.recvlineS())
s = (r + c * x) % (p - 1)
io.sendlineafter(b"s = ", str(s).encode())
print(io.recvallS())
# ictf{w34k_n0nc3_gEn3r4t1on_smh}
