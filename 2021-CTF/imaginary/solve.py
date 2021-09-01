from pwn import remote
import ast
from operator import add, sub

io = remote("chal.imaginaryctf.org", 42015)
io.recvuntil(b"so watch out!)\n\n")

for i in range(300):
    q = io.recvlineS().strip()
    print(i, q)
    if "import" in q:
        io.sendlineafter(b"> ", "c8763")
        io.recvuntil(b"Correct!\n")
        continue
    toks = q.split(" ")
    nums = [ast.literal_eval(x.replace("i", "j")) for x in toks[::2]]
    ops = [add] + [add if x == "+" else sub for x in toks[1::2]]
    ans = 0
    for i in range(len(ops)):
        ans = ops[i](ans, nums[i])
    sans = str(ans).replace("(", "").replace(")", "").replace("j", "i")
    print(ans, sans)
    io.sendlineafter(b"> ", sans)
    io.recvuntil(b"Correct!\n")
io.interactive()
