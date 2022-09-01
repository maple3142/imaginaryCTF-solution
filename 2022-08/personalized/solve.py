from pwn import *
from sage.all import crt

def get(seed):
    # io = process(['python', 'enc.py'])
    io = remote("puzzler7.imaginaryctf.org", 4002)
    io.sendlineafter(b'>>> ', seed.to_bytes(4, 'big'))
    io.recvuntil(b'n = ')
    n = int(io.recvline())
    io.recvuntil(b'e = ')
    e = int(io.recvline())
    io.recvuntil(b'c = ')
    c = int(io.recvline())
    io.close()
    return n, e, c

seed = 4284536744
e = 19
ns = []
cs = []
for _ in range(e):
    n, ee, c = get(seed)
    assert ee == e
    ns.append(n)
    cs.append(c)

m = crt(cs, ns).nth_root(e)
print(int(m).to_bytes((m.nbits() + 7) // 8, 'big'))
# ictf{just_f0r_y0uuuuuuuu}

"""
other good seeds:
4213973159 -> 0
10000001027800207 -> 0
bytes_to_long(b'aanpxlwku') -> 0
"""
