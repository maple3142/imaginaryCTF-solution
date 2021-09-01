from Crypto.Util.number import *
from z3 import *


def nor(a, b):
    return ~(a | b)


def bit(bv, i):
    return Extract(i, i, bv)


def bit2(bv, i, j):
    return Extract(i, j, bv)


def nora(inp):
    assert inp.size() == 3
    out = [None] * 2
    w1 = nor(bit(inp, 0), bit(inp, 1))
    w2 = nor(bit(inp, 0), w1)
    w3 = nor(bit(inp, 1), w1)
    w4 = nor(w2, w3)
    w5 = nor(w4, w4)
    w6 = nor(w5, bit(inp, 2))
    w7 = nor(w5, w6)
    w8 = nor(bit(inp, 2), w6)
    w9 = nor(w7, w8)
    out[0] = nor(w9, w9)
    w10 = nor(bit(inp, 0), bit(inp, 0))
    w11 = nor(bit(inp, 1), bit(inp, 1))
    w12 = nor(w10, w11)
    w13 = nor(bit(inp, 2), bit(inp, 2))
    w14 = nor(w11, w13)
    w15 = nor(w12, w14)
    w16 = nor(w10, w13)
    w17 = nor(w15, w15)
    w18 = nor(w17, w16)
    out[1] = nor(w18, w18)
    return out[::-1]


def norb(inp):
    assert inp.size() == 33
    out = [None] * 17
    w1, out[0] = nora(Concat(bit(inp, 32), bit(inp, 16), bit(inp, 0)))
    w2, out[1] = nora(Concat(w1, bit(inp, 1), bit(inp, 17)))
    w3, out[2] = nora(Concat(w2, bit(inp, 18), bit(inp, 2)))
    w4, out[3] = nora(Concat(w3, bit(inp, 3), bit(inp, 19)))
    w5, out[4] = nora(Concat(w4, bit(inp, 20), bit(inp, 4)))
    w6, out[5] = nora(Concat(w5, bit(inp, 5), bit(inp, 21)))
    w7, out[6] = nora(Concat(w6, bit(inp, 22), bit(inp, 6)))
    w8, out[7] = nora(Concat(w7, bit(inp, 7), bit(inp, 23)))
    w9, out[8] = nora(Concat(w8, bit(inp, 24), bit(inp, 8)))
    w10, out[9] = nora(Concat(w9, bit(inp, 9), bit(inp, 25)))
    w11, out[10] = nora(Concat(w10, bit(inp, 26), bit(inp, 10)))
    w12, out[11] = nora(Concat(w11, bit(inp, 11), bit(inp, 27)))
    w13, out[12] = nora(Concat(w12, bit(inp, 28), bit(inp, 12)))
    w14, out[13] = nora(Concat(w13, bit(inp, 13), bit(inp, 29)))
    w15, out[14] = nora(Concat(w14, bit(inp, 30), bit(inp, 14)))
    out[16], out[15] = nora(Concat(w15, bit(inp, 15), bit(inp, 31)))
    return out[::-1]


def norc(inp):
    assert inp.size() == 513
    out = [None] * 257
    w1, *out[15::-1] = norb(
        Concat(bit(inp, 512), bit2(inp, 271, 256), bit2(inp, 15, 0))
    )
    w2, *out[31:15:-1] = norb(Concat(w1, bit2(inp, 31, 16), bit2(inp, 287, 272)))
    w3, *out[47:31:-1] = norb(Concat(w2, bit2(inp, 303, 288), bit2(inp, 47, 32)))
    w4, *out[63:47:-1] = norb(Concat(w3, bit2(inp, 63, 48), bit2(inp, 319, 304)))
    w5, *out[79:63:-1] = norb(Concat(w4, bit2(inp, 335, 320), bit2(inp, 79, 64)))
    w6, *out[95:79:-1] = norb(Concat(w5, bit2(inp, 95, 80), bit2(inp, 351, 336)))
    w7, *out[111:95:-1] = norb(Concat(w6, bit2(inp, 367, 352), bit2(inp, 111, 96)))
    w8, *out[127:111:-1] = norb(Concat(w7, bit2(inp, 127, 112), bit2(inp, 383, 368)))
    w9, *out[143:127:-1] = norb(Concat(w8, bit2(inp, 399, 384), bit2(inp, 143, 128)))
    w10, *out[159:143:-1] = norb(Concat(w9, bit2(inp, 159, 144), bit2(inp, 415, 400)))
    w11, *out[175:159:-1] = norb(Concat(w10, bit2(inp, 431, 416), bit2(inp, 175, 160)))
    w12, *out[191:175:-1] = norb(Concat(w11, bit2(inp, 191, 176), bit2(inp, 447, 432)))
    w13, *out[207:191:-1] = norb(Concat(w12, bit2(inp, 463, 448), bit2(inp, 207, 192)))
    w14, *out[223:207:-1] = norb(Concat(w12, bit2(inp, 223, 208), bit2(inp, 479, 464)))
    w15, *out[239:223:-1] = norb(Concat(w14, bit2(inp, 495, 480), bit2(inp, 239, 224)))
    out[256], *out[255:239:-1] = norb(
        Concat(w15, bit2(inp, 255, 240), bit2(inp, 511, 496))
    )
    return out[::-1]


x1 = int("1a86f06e4e492e2c1ea6f4d5726e6d36bec57cf31472b986a675d3bc8e5d22b81", 16)
x2 = int(
    "1a5e20394c934fd1198b1517d57e730cd225ccfa064ff42db76c19f3b7c0da91a6bf077b696cc4b22c0e56f4d3e6e150e386d6f04479ac502600e01fcdc29f5e4",
    16,
)


def abnormal(inp):
    assert inp.size() == 256
    w1 = Concat(norc(Concat(BitVecVal(x1, 257), inp))[255::-1])
    w2 = Concat(norc(BitVecVal(x2, 513))[255::-1])
    w3 = nor(w1, w2)
    w4 = nor(w1, w3)
    w5 = nor(w2, w3)
    w6 = nor(w4, w5)
    out = nor(w6, w6)
    return out


flag = BitVec("flag", 256)
sol = Solver()
sol.add(abnormal(flag) == 0)
while sol.check() == sat:
    m = sol.model()
    ans = m[flag].as_long()
    print(long_to_bytes(ans))
    sol.add(flag != ans)
