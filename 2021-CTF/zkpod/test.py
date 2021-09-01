#!/usr/local/bin/python
from Crypto.Util.number import bytes_to_long, getRandomRange, long_to_bytes
import hashlib
from sage.all import *

N = 0xA31051588DBFDA644F251DAFC69806D4A9119BA5388B4A6CBE95C0E3B6FA5CAD332330EBCF2BF6B563C3777615EDEF97FF9001E607C2DF30C1C197D2298B62F3F60B9A8AD48E81DE6E3DD7F9AC709F2C9656C377E6BC613FC6F49ADAD91A52C7DB6A591CFBFA783AA0EECBE0CEDB6E4431D3C07A88420209AFFC654B2B7D17C756130BA6CEBCE813F73E05EFB430AB48BC1378D5D4B31D44C3E06870F5C927A189EA8E60DBC295CC753FC122EDB86EFDCA812DB0774A4E9A5EE27079A2DA91B61EC183A2A3BACDF557EBA6ED274CEAE7A00E28F212E225238A09667856A431179C76E06911506E4B93EE8D9874957BD301A28B7D61A52B60CCF978129674B6ED
e = 0x10001
P = 0x199E1926F2D2D5967B1D230B33DE0A249F958E5B962F8B82CA042970180FE1505607FE4C8CDE04BC6D53AEC53B4AA25255AE67051D6ED9B602B1B19E128835B20227DB7EE19CF88660A50459108750F8B96C71847E4F38A79772A089AA46666404FD671CA17EA36EE9F401B4083F9CA76F5217588C6A15BABA7EB4A0934E2026937812C96E2A5853C0E5A65231F3EB9FDC283E4177A97143FE1A3764DC87FD6D681F51F49F6EED5AB7DDC2A1DA7206F77B8C7922C5F4A5CFA916B743CEEDA943BC73D821D2F12354828817FF73BCD5800ED201C5AC66FA82DF931C5BBC76E03E48720742FFE673B7786E40F243D7A0816C71EB641E5D58531242F7F5CFEF60E5B
g = 2

flag = 4876348763

d = 0x116FCD430AE5591520E1772B34B14D09B08A917A3971ABA3B53D8E42CB6E3A3ACB1D183E1F093478711295D3AAC4A6BA3A39CBFA2D1A49838D34866792C9B4EB21845C223C5880CAA83F34B91E176CEDF7A58F8162CB021B2FCB3843EEB341E6DD2FA217D75A114133B45558D4C5E224A8AF5C05BE4C50AB788624CEC4F7BB730924D926282BD0819E2DDFEA5B870E6EA2D85DE5776C1954342817151AC2C291A5C28A7023B671169FABCD50D7675C4BA546A374D6DF624E920E1F9C82E05A4340233C5807D9E499E06DD9C5032F8C876D4052A4EC6723CD4BFD7850068D94FB65A6849D933CF3F8B2AFA70DFB1B414656A373FDCF3B8E3B599A4EAA7535281


def decrypt(c):
    return pow(c, d, N)


def H(x):
    return bytes_to_long(
        hashlib.sha512(b"domain" + x).digest()
        + hashlib.sha512(b"separation" + x).digest()
    )


def sign(x):
    k = getRandomRange(0, (P - 1) // 2)
    r = pow(g, k, P)
    e = H(str(r).encode() + b"Haha, arbitrary message")
    s = (k - x * e) % (P - 1)
    return r, s, k


# print(f"Here's my encrypted flag: {hex(pow(flag, e, N))}")
# print(
#     "To prove that I can correctly decrypt whatever you send to me, I'll use decryptions to sign messages"
# )
# while True:
#     print("> ", end="")
#     c = int(input(), 16)
#     m = decrypt(c)
#     print("dec", m)
#     r, s = sign(m)
#     print(f"r: {r}")
#     print(f"s: {s}")


def HH(r):
    return H(str(r).encode() + b"Haha, arbitrary message")


flag = 4876387871111111111111111111111111111

encflag = pow(flag, e, N)
r1, s1, kk1 = sign(decrypt(encflag))
e1 = HH(r1)
assert r1 == pow(g, s1 + decrypt(encflag) * e1, P)
assert s1 == kk1 - flag * e1

encflag = pow(flag, e, N)
r2, s2, kk2 = sign(decrypt(encflag))
e2 = HH(r2)
assert r2 == pow(g, s2 + decrypt(encflag) * e2, P)
assert s2 == kk2 - flag * e2

assert e2 * s1 - e1 * s2 == e2 * kk1 - e1 * kk2  # integer

PP = PolynomialRing(ZZ, "k1,k2,x")
k1, k2, x = PP.gens()
f1 = s1 - (k1 * e1 + (s1 % e1) - x * e1)
assert f1(kk1 // e1, 0, flag) == 0
f2 = s2 - (k2 * e2 + (s2 % e2) - x * e2)
assert f2(0, kk2 // e2, flag) == 0

# f1 = s1 - ((k1 + kk1 // e1) * e1 + (s1 % e1) - x * e1)
# assert f1(0, 0, flag) == 0
# f2 = s2 - ((k2 + kk2 // e2) * e2 + (s2 % e2) - x * e2)
# assert f2(0, 0, flag) == 0
# a, b, c = f.coefficients()
# print(a, b, c)
# print(a * (kk1 // e1) + b * flag + c)
# print(kk1 // e1, flag)
# K = 2 ** 1024
# M = Matrix(ZZ, [[c, 0, 0], [a, 1, 0], [b+1, 0, 1]])
# for row in M.LLL():
#     print(row)

# assert kk1%e1==s1%e1
# PP = PolynomialRing(ZZ, 'k1hx')
# k1hx = PP.gen()
# f = s1-((k1hx)*e1+(s1%e1))
# assert f(kk1 // e1 - flag) == 0
# k1hx=f.roots()[0][0]

from sage.matrix.matrix2 import Matrix

# print((power_mod(g, e2 * s1 - e1 * s2, P) * power_mod(r2, e1, P)) % P)
# print(power_mod(r1, e2, P))


def resultant(f1, f2, var):
    # Copied from https://jsur.in/posts/2021-07-19-google-ctf-2021-crypto-writeups
    return Matrix.determinant(f1.sylvester_matrix(f2, var))


# P = PolynomialRing(GF(P), "x,k1,k2,k3")
# x, k1, k2, k3 = P.gens()

# f1 = s1 - (k1 - x * e1)
# f2 = s2 - (k2 - x * e2)
# f3 = s3 - (k3 - x * e3)

# assert f1.subs(k1=kk1, x=flag) == 0
# assert f2.subs(k2=kk2, x=flag) == 0
# assert f3.subs(k3=kk3, x=flag) == 0

# g1 = resultant(f1, f2, x)
# g2 = resultant(f2, f3, x)
# g3 = resultant(f1, f3, x)
# # print(g1)
# # print()
# # print(resultant(g2, g3, k3))
# # print()
# print(resultant(g1, resultant(g2, g3, k3), k1))


# exit()

# N = 0xBB00128C1C1555DC8FC1CD09B3BB2C3EFEAAE016FCB336491BD022F83A10A501175C044843DBEC0290C5F75D9A93710246361E4822331348E9BF40FC6810D5FC7315F37EB8F06FB3F0C0E9F63C2C207C29F367DC45EEF2E5962EFF35634B7A29D913A59CD0918FA395571D3901F8ABD83322BD17B60FD0180358B7E36271ADCFC1F9105B41DA6950A17DBA536A2B600F2DC35E88C4A9DD208AD85340DE4D3C6025D1BD6E03E9449F83AFA28B9FF814BD5662018BE9170B2205F38CF3B67BA5909C81267DAA711FCDB8C7844BBC943506E33F5F72F603119526072EFBC5CEAE785F2AF634E6C7D2DD0D51D6CFD34A3BC2B15A752918D4090D2CA253DF4EF47B8B
# e = 0x10001
# P = 0x199E1926F2D2D5967B1D230B33DE0A249F958E5B962F8B82CA042970180FE1505607FE4C8CDE04BC6D53AEC53B4AA25255AE67051D6ED9B602B1B19E128835B20227DB7EE19CF88660A50459108750F8B96C71847E4F38A79772A089AA46666404FD671CA17EA36EE9F401B4083F9CA76F5217588C6A15BABA7EB4A0934E2026937812C96E2A5853C0E5A65231F3EB9FDC283E4177A97143FE1A3764DC87FD6D681F51F49F6EED5AB7DDC2A1DA7206F77B8C7922C5F4A5CFA916B743CEEDA943BC73D821D2F12354828817FF73BCD5800ED201C5AC66FA82DF931C5BBC76E03E48720742FFE673B7786E40F243D7A0816C71EB641E5D58531242F7F5CFEF60E5B
# g = 2

# import gmpy2

# g = gmpy2.mpz(2)
# P = gmpy2.mpz(P)


# r, s, k = sign(4848763)
# ee = H(str(r).encode() + b"Haha, arbitrary message")
# gs = gmpy2.powmod(g, s, P)
# r_gs = (r * gmpy2.invert(gs, P)) % P
# ge = gmpy2.powmod(g, ee, P)

# f = 221464237
# cf = (P - 1) // f

# Z = Zmod(P)

# print("dlog")
# d = discrete_log_rho(Z(r_gs), Z(ge), ord=f)
# print(d)
# print(long_to_bytes(d))
