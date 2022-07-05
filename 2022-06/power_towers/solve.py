from random import Random, randint
from pwn import process, remote, unbits, context
from sage.all import GF
from tqdm import tqdm


def find_seed(i, n):
    while True:
        seed = randint(1, 487634876348763)
        r = Random(seed)
        ar = list(range(n))
        r.shuffle(ar)
        if ar[0] == i:
            return seed


# io = process(["python", "tot.py"])
io = remote("puzzler7.imaginaryctf.org", 2005)
io.recvuntil(b"is: ")
p = int(io.recvline())
F = GF(p)
od5 = F(5).multiplicative_order()
od3 = F(3).multiplicative_order()
print(od5)
print(od3)
if od5 <= od3:
    print("try again")
    exit(0)


def get_hash(seed):
    io.sendline(str(seed).encode())
    io.recvuntil(b"is ")
    return int(io.recvline())


n = 256
bits = []
for i in tqdm(range(n)):
    seed = find_seed(i, n)
    h = get_hash(seed)
    if F(h) ** od3 != 1:
        bits.append(1)
    else:
        bits.append(0)
print(unbits(bits))
# ictf{p0wer_t0w3rs_4r3_gr34t!!!!}


"""
This is unintended, the intended one is:
```
https://imaginaryctf.org/f/j8iGv#x.py

Since iterating the carmichael lambda function leads to 1 very quickly for most numbers(for numbers of size close to 2^64(the size here doesn't really matter, i chose to make it a bit small so that the totients could be calculated pretty quickly), the amount of iterations is usually about 10) the power tower function actually only cares about the first 10-ish numbers in the list given to it. So, by shuffling the flag in various ways, after enough queries each bit of the flag will be among the first 10(which we can recover by just trying all 2^10 options), meaning that it will be possible to recover. To decrease the amount of queries necessary, we can choose the seed a bit more carefully so that the first 10 bits of the shuffled flag have as many unknown bits as possible.
```

To fix this unintended, choosing p=4*prime+1 and p=17 (mod 60) will ensure that 3, 5 are primitive root modulo p.
Author's explanation:
```
2 mod 15: if p=15k+2, then x^(15(14k+1))=x^(15*14k+15)=x^(14p-13)=x, so you can't determine the second number
for not being able to determine the first number, i want 3 and 5 to be primitive roots
to do that, i first make it (power of 2)*prime+1, so a number is only not a primitive root if it's -1 or a quadratic residue
p being 2 mod 15 already achieves 5 not being a quadratic residue, and if i make it 17 mod 60 then 3 alos won't be a quadratic residue, if it's 17 mod 60 then it clearly can't be 2*prime+1 so we can require 4*prime+1 
```

My notes:
p=2 (mod 15) ensures that 5 is a quadratic non residue modulo p can be proved by https://en.wikipedia.org/wiki/Quadratic_reciprocity
using the same theorem can derive that p=-1 (mod 3) and (p-1)//2 is divides by 2 could ensure legendre(3,p)=-1
and p^2=-1 (mod 5) is enough to ensure legendre(5,p)=-1
"""
