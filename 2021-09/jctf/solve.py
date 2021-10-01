import string

with open("flag", "rb") as f:
    data = f.read()

data = bytes(
    [x for x in data if x in (string.printable).encode() and x not in b"\n"]
).replace(b"[1A", b"")
print(data)
