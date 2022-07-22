import re

t = lambda *a: bytes.fromhex("{:x}".format(a[0])).decode()

with open("test.py", "r") as f:
    s = f.read()

    def subfn(m):
        r = t(eval(m.group(1)))
        return repr(r)

    s = re.sub(r"t\(([0-9+ ]+)\)", subfn, s)
print(s)
# python repace_t.py > test2.py
