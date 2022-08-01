from pwn import *
import numpy as np

with open('flag.txt', 'rb') as f:
    ar = []
    for l in f:
        ar.append(bits(l.strip()))
    A = np.array(ar)

cbits = []
for i, col in enumerate(A.T):
    if len(set(col)) == 2:
        # print(i, set(col))
        cbits.append(i)
np.set_printoptions(threshold=sys.maxsize, linewidth=10000)
# print(A)
print(A[:, cbits].T)
