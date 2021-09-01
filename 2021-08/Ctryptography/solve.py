from pwn import remote


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


io = remote("puzzler7.imaginaryctf.org", 6666)
io.recvuntil(b"flag: ")
enc_flag = bytes.fromhex(io.recvlineS().strip())
pt = b"a" * len(enc_flag)
while True:
    io.sendlineafter(b"encrypt? ", pt)
    enc = bytes.fromhex(io.recvlineS().strip())
    flag = xor(xor(enc, enc_flag), pt)
    print(flag)
    if flag.startswith(b"ictf{"):
        break
