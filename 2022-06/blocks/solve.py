with open("blocks.txt") as f:
    s = f.read()

bits = [int(x == "█") for x in s]
flag = "".join(
    chr(int("".join(map(str, bits[i : i + 8])), 2)) for i in range(0, len(bits), 8)
)
print(flag)
# ictf{bl0ckbuster_b1nary_19bba002}
