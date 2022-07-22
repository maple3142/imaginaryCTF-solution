import re

t = lambda *a: bytes.fromhex("{:x}".format(a[0])).decode()

with open("test2.py", "r") as f:
    s = f.read()

    def subfn(m):
        r = int(m.group(1))
        return '[' + str(r%8) + ']'

    s = re.sub(r"\[(\d+?)\]", subfn, s)
print(s)
# python replace_g.py > test3.py
