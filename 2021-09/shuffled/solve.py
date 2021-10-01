import random

with open("out.txt") as f:
    enc = f.read()


def get_stream(seed):
    random.seed(seed)
    for i in range(len(enc) - 1, -1, -1):
        yield random.randint(0, i)


for a in range(256):
    for b in range(256):
        tmp = list(enc)
        seed = bytes([a, b])
        rev = iter(list(get_stream(seed))[::-1])
        for i in reversed(range(len(enc) - 1, -1, -1)):
            j = next(rev)
            tmp[i], tmp[j] = tmp[j], tmp[i]
        plain = "".join(tmp)
        if "flag" in plain:
            with open(f"output/{a}_{b}.txt", "w") as f:
                f.write(plain)

# then `cat output/*` to find which looks like a English paragraph
# flag: echo "ictf{$(md5sum output/60_9.txt | awk '{print $1}')}"
