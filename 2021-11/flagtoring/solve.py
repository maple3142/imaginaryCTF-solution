from math import gcd
from Crypto.Util.number import long_to_bytes

n = 1528656555903550344116452290097825083432239562289311449762856110644178238847468718159931142582566958406852960634326674294592831730135914025243113420620191820735271996685130044674881553230289164686150060478587182721212339660071286119
e = 764328277951775172058226145048912541716119781144655724881428055322089119423734359079965571291283479203426480317163292925665158834567666283670763086349732720212733069060883710729256895758575480803498007307124796853534451106915539873

# e = 1 (mod phi(n))
# e - 1 = k * phi(n)


def two_powers(x):
    i = 0
    while x % 2 == 0:
        x //= 2
        i += 1
    return i


def factor_with_phi(n, phi, upper_bound=100):
    # See 8.2.2(i) in Handbook of Applied Cryptography
    s = two_powers(phi)
    t = phi // (2 ** s)
    for a in range(2, upper_bound):
        k = t
        while k < phi:
            ak = pow(a, k, n)
            ak2 = (ak * ak) % n
            if ak != 1 and ak != n - 1 and ak2 == 1:
                p = gcd(ak - 1, n)
                if p == 1:
                    continue
                assert n % p == 0
                q = n // p
                return p, q
            k *= 2


p, q = factor_with_phi(n, e - 1)
print(long_to_bytes(p >> 2))
print(long_to_bytes(q >> 2))

# ictf{dumb_3xp0nent_but_you_g0tt4_fl4gt0r_1t_t0o}
