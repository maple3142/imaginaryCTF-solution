from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    freq: int
    is_leaf: bool = False
    sparent: Node = None
    left: Node = None
    right: Node = None


def insert(tree: Node, node: Node):
    if tree is None:
        return node
    if node.freq > tree.freq:
        v4 = tree
        i = tree.sparent
        while i is not None and i.freq < node.freq:
            v4 = i
            i = i.sparent
        v4.sparent = node
        node.sparent = i
        return tree
    else:
        node.sparent = tree
        return node


freq = [0] * 256
with open("fake_flag.txt", "rb") as f:
    for b in f.read():
        freq[b] += 1
tree: Node = None
for i in range(256):
    if freq[i]:
        node = Node(i, freq[i], True)
        tree = insert(tree, node)
t = tree
while t:
    print(t.val, t.freq)
    t = t.sparent

while tree.sparent:
    left = tree
    right = tree.sparent
    print('merge', left.val, right.val)
    node = Node(f'(sum={left.freq + right.freq}, left={left.val}, right={right.val})', left.freq + right.freq, False, None, left, right)
    tree = insert(tree.sparent.sparent, node)
print(tree.val)
