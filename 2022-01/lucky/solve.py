from pwn import *
from tqdm import tqdm

# io = process(["python", "main.py"])
io = remote("chal.imaginaryctf.org", 42050)
for _ in tqdm(range(200)):
    io.recvuntil(b"is: ")
    key = int(io.recvlineS().strip())
    key = str((key + 10000000000) ^ 1337)
    password = "".join([chr(int(key[i : i + 2])) for i in range(0, len(key), 2)])
    io.sendline(password.encode())
io.interactive()

# ictf{$imp13_pwn700ls_ch@113ng3_62302d5c}
