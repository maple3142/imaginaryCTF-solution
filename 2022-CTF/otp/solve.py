from pwn import *
import numpy as np
from tqdm import tqdm

# io = process(["python", "otp.py"])
io = remote("otp.chal.imaginaryctf.org", 1337)
T = 128
cts = []
for _ in tqdm(range(T)):
    io.sendlineafter(b"Enter plaintext: ", b"FLAG")
    io.recvuntil(b"Encrypted flag: ")
    ct = bytes.fromhex(io.recvlineS().strip())
    cts.append(bits(ct))

print(unbits((np.array(cts).T.sum(axis=1) < T // 2) * 1))
# \xe9ctf{benfords_law_catching_tax_fraud_since_1938}
# ictf{benfords_law_catching_tax_fraud_since_1938}
