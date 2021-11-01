from pwn import remote
from hashlib import sha3_256


io = remote("puzzler7.imaginaryctf.org", 7331)
io.sendlineafter(b">>> ", b"\x7f")
io.recvuntil(b"admin: ")
h_admin = io.recvline().strip()
print(h_admin)

io.recvuntil(b"('")
salt = io.recvuntil(b"')")[:-2]

print(salt)


def H(b: bytes):
    return sha3_256(b + salt).hexdigest()


io.sendlineafter(b"continue", b"\n")
io.sendlineafter(b">>> ", b"1")
io.sendlineafter(b"username: ", b"admin")
io.recvuntil(b"'")
sfx = io.recvuntil(b"'")[:-1]
io.sendlineafter(b"result:", H(h_admin + sfx).encode())
io.sendlineafter(b">>> ", b"3")
print(io.recvlineS().strip())
