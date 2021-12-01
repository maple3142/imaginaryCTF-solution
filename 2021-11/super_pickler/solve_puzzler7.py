#!/usr/bin/env python3.9

import pickle
import marshal
from dis import dis
from copy import deepcopy

# from tree import Tree

def unpick(b, clss):
    d = pickle.loads(b)
    obj = pickle.loads(d["__"])
    for key in d:
        if key != "__":
            obj.__setattr__(key, lambda x:x)
            obj.__getattribute__(key).__setattr__("__code__", marshal.loads(d[key]))
            setattr(clss, key, lambda x,y:x)
            setattr(getattr(clss, key), "__code__", marshal.loads(d[key]))

    return obj

def tree_map(d, a, b):
    if a.data == None:
        return
    d[a.data] = b.data
    tree_map(d, a.left, b.left)
    tree_map(d, a.right, b.right)

flag = unpick(open("pick", "rb").read(), Tree)
x = Tree(''.join(chr(i) for i in range(32,32+len(flag))))

d = {}
tree_map(d, x, flag)
out = ['~']*len(flag)
for key in d:
    out[ord(key)-32] = d[key]
print(''.join(out))