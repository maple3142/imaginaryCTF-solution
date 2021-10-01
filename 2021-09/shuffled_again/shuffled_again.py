import random, os, string

def shuffle(plain):
    plain = list(plain)
    for i in range(len(plain) - 1, -1, -1):
        j = random.randint(0, i)
        plain[i], plain[j] = plain[j], plain[i]
    return ''.join(plain)

alphabet = string.ascii_lowercase

with open("seed.bin", "rb") as s:
    s1 = s.read(2)
    s2 = s.read(16)

assert s1[0] >= 128

with open("plain.txt") as f:
    random.seed(s1)
    plain = shuffle(''.join(c for c in f.read().lower() if c in alphabet))

    random.seed(s2)
    shuf = shuffle(alphabet)
    plain = plain.translate(''.maketrans(alphabet, shuf))

with open("out.txt", "w") as f:
    f.write(plain)

print(f"The flag is ictf{{{shuf}{s1.hex()}}}, you might want to try solving `shuffled` first...")
