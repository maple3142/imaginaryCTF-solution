from PIL import Image
import numpy as np

img = Image.open("RGB.png")
ar = np.asarray(img)


def f(ar):
    block_size = 75
    tot = 600
    ret = []
    for i in range(0, tot, block_size):
        tmp = []
        for j in range(0, tot, block_size):
            tmp.append(ar[i, j])
        ret.append(tmp)
    return np.array(ret)


ar = f(ar)


s = ""
for i in range(8):
    for j in range(8):
        r = ar[i, j, 0] & 1
        g = ar[i, j, 1] & 1
        b = ar[i, j, 2] & 1
        x = (r << 2) | (g << 1) | b
        s += str(x)

flag = ""
tmp = ""
while s:
    tmp += s[0]
    s = s[1:]
    v = int(tmp, 8)
    if 20 <= v < 127:
        flag += chr(v)
        tmp = ""
print(flag)
