import random
with open("plain.txt") as f:
    plain = list(f.read())

with open("seed.bin", "rb") as f:
    random.seed(f.read(2))

for i in range(len(plain) - 1, -1, -1):
    j = random.randint(0, i)
    plain[i], plain[j] = plain[j], plain[i]

with open("out.txt", "w") as f:
    f.write(''.join(plain))
