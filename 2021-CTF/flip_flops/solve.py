from pwn import *


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# io = process(["python", "7B4E-flop.py"])
io = remote("chal.imaginaryctf.org", 42011)
io.sendlineafter(b"> ", "1")
io.sendlineafter(b"Enter your plaintext (in hex): ", (b"a" * 32).hex())
data = bytes.fromhex(io.recvlineS().strip())
iv, ct = data[:16], data[16:]
x = xor(iv, b"a" * 16)
iv = xor(x, b"gimmeflag       ")
data = iv + ct
io.sendlineafter(b"> ", "2")
io.sendlineafter(b"Enter ciphertext (in hex): ", data.hex())
io.interactive()
