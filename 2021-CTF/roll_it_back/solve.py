from itertools import *
from functools import reduce
from gmpy2 import *
from z3 import *
from tqdm import tqdm
from Crypto.Util.number import *


def x(a, b):
    return bytes(
        islice((x ^ y for x, y in zip(cycle(a), cycle(b))), max(*map(len, [a, b])))
    )


def t(x):
    return sum((((x & 28) >> 4) & 1) << i for i, x in enumerate(x))


T = t(x(b"jctf{not_the_flag}", b"*-*")) | 1
l = 420


def popcount(b):
    n = b.size()
    bits = [Extract(i, i, b) for i in range(n)]
    bvs = [Concat(BitVecVal(0, n - 1), b) for b in bits]
    nb = reduce(lambda a, b: a + b, bvs)
    return nb


def rev(x, n):
    flag = BitVec("flag", l)
    iflag = flag
    sol = Solver()
    for _ in range(n):
        flag = LShR(flag, 1) | ((popcount(flag & T) & 1) << (l - 1))
    sol.add(flag == x)
    assert sol.check() == sat
    m = sol.model()
    return m[iflag].as_long()


flag = 2535320453775772016257932121117911974157173123778528757795027065121941155726429313911545470529920091870489045401698656195217643
for i in tqdm(range(421337 // 10)):
    flag = rev(flag, 10)
for _ in range(7):
    flag = rev(flag, 1)
print(flag)
print(long_to_bytes(flag)[::-1])
