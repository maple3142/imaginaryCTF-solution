import pickle
import pickletools

with open("flag", "rb") as f:
    data = f.read()


class Node:
    pass


def get_len(l):
    x = 0
    y = l
    while y is not None:
        x += 1
        y = y.data
    return x


lst = pickle.loads(data)

cur = lst
while cur is not None:
    print(chr(get_len(cur)), end="")
    cur = cur.next
