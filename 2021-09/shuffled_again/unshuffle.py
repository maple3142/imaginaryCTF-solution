import random


def unshuffle(plain):
    plain = list(plain)
    js = []
    for i in range(len(plain) - 1, -1, -1):
        j = random.randint(0, i)
        js.append(j)
    for i, j in reversed(list(zip(range(len(plain) - 1, -1, -1), js))):
        plain[i], plain[j] = plain[j], plain[i]
    return "".join(plain)


with open("out.txt", "r") as f:
    ct = f.read()

for a in range(128, 256):
    print(a)
    for b in range(256):
        random.seed(bytes([a, b]))
        with open(f"unshuffled/{a}-{b}.txt", "w") as f:
            f.write(unshuffle(ct))
