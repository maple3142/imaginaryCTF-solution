from pwn import remote
from Crypto.Util.number import *
from sage.all import *

N = 0xBB00128C1C1555DC8FC1CD09B3BB2C3EFEAAE016FCB336491BD022F83A10A501175C044843DBEC0290C5F75D9A93710246361E4822331348E9BF40FC6810D5FC7315F37EB8F06FB3F0C0E9F63C2C207C29F367DC45EEF2E5962EFF35634B7A29D913A59CD0918FA395571D3901F8ABD83322BD17B60FD0180358B7E36271ADCFC1F9105B41DA6950A17DBA536A2B600F2DC35E88C4A9DD208AD85340DE4D3C6025D1BD6E03E9449F83AFA28B9FF814BD5662018BE9170B2205F38CF3B67BA5909C81267DAA711FCDB8C7844BBC943506E33F5F72F603119526072EFBC5CEAE785F2AF634E6C7D2DD0D51D6CFD34A3BC2B15A752918D4090D2CA253DF4EF47B8B
e = 0x10001
P = 0x199E1926F2D2D5967B1D230B33DE0A249F958E5B962F8B82CA042970180FE1505607FE4C8CDE04BC6D53AEC53B4AA25255AE67051D6ED9B602B1B19E128835B20227DB7EE19CF88660A50459108750F8B96C71847E4F38A79772A089AA46666404FD671CA17EA36EE9F401B4083F9CA76F5217588C6A15BABA7EB4A0934E2026937812C96E2A5853C0E5A65231F3EB9FDC283E4177A97143FE1A3764DC87FD6D681F51F49F6EED5AB7DDC2A1DA7206F77B8C7922C5F4A5CFA916B743CEEDA943BC73D821D2F12354828817FF73BCD5800ED201C5AC66FA82DF931C5BBC76E03E48720742FFE673B7786E40F243D7A0816C71EB641E5D58531242F7F5CFEF60E5B
g = 2

io = remote("chal.imaginaryctf.org", 42012)
# io = process('python')
io.recvuntil(b"Here's my encrypted flag: ")
encflag = int(io.recvlineS().strip(), 16)


def sign_dec(ct):
    global io
    try:
        io.sendlineafter(b"> ", hex(ct))
        io.recvuntil(b"r: ")
        r = int(io.recvlineS().strip())
        io.recvuntil(b"s: ")
        s = int(io.recvlineS().strip())
        return r, s
    except:
        io.close()
        io = remote("chal.imaginaryctf.org", 42012)
        return sign_dec(ct)


from gmpy2 import powmod
import hashlib
from Crypto.Util.number import bytes_to_long


def H(x):
    return bytes_to_long(
        hashlib.sha512(b"domain" + x).digest()
        + hashlib.sha512(b"separation" + x).digest()
    )


def HH(r):
    return H(str(r).encode() + b"Haha, arbitrary message")


def oracle(x):
    # s = k - x * H(r || d)
    r, s = sign_dec(x)
    ep = HH(r) % 2
    if ep % 2 == 0:
        return
    # s = k - x (mod 2)
    # x = k - s (mod 2)
    # kronecker(g, P) = -1
    kp = 1 if kronecker(r, P) == -1 else 0
    sp = s % 2
    return (kp - sp) % 2


def crack(c, n, e, oracle, lim=1000):
    c0 = c
    c2 = pow(2, e, n)
    l, r = 0, n
    while r - l > lim:
        # Due to rounding problem, it can't really get an accurate answer...
        mid = (l + r) // 2
        ret = oracle((c2 * c) % n)
        if ret is None:
            continue
        if ret == 0:
            r = mid
        else:
            l = mid
        c = (c2 * c) % n
        print(r - l)
    for x in range(l, r + 1):
        if powmod(x, e, n) == c0:
            return x


print(long_to_bytes(crack(encflag, N, e, oracle, 10000)))
# ictf{gr0up5_should_b3_pr1me_0rd3r_dummy}
