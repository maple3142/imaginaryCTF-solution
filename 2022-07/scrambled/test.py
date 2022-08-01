import ctypes

libc = ctypes.CDLL('libc.so.6')

def scramble(buf, ln):
    for i in range(ln):
        a = libc.rand()%ln
        b = libc.rand()%ln
        buf[a],buf[b]=buf[b],buf[a]

def unscramble(buf, ln):
    aa = []
    bb = []
    for i in range(ln):
        aa.append(libc.rand()%ln)
        bb.append(libc.rand()%ln)
    aa.reverse()
    bb.reverse()
    for i in range(ln):
        buf[aa[i]],buf[bb[i]]=buf[bb[i]],buf[aa[i]]


# spos = list(range(8))
# scramble(spos, len(spos))
# print(spos)
# b = bytearray(b'pekomiko')
# print(b)
# unscramble(b, len(b))
# print(b)

b = bytearray(b'pkmokeio')
scramble(b, len(b))
print(b)
