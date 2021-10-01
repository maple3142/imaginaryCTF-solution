from pwn import remote

p = 95448141706840057074981648919653158061602940212059310641262844843045070085413
g = 2
r = p - 1

io = remote("67.159.89.33", 18000)
io.sendlineafter(b"c = ", b"1")
io.recvuntil(b"s = ")
s = int(io.recvlineS())
print(s)
y = pow(g, s, p)
key = (s - r) % (p - 1)
print(key)
assert pow(g, key, p) == y
io.sendlineafter(b"t = ", b"1")
io.recvuntil(b"c = ")
c = int(io.recvlineS())
s = (key * c) % (p - 1)
io.sendlineafter(b"s = ", str(s).encode())
io.interactive()

# ictf{w45_1t_tru1y_r4ndom..?}
