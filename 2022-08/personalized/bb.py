import random

while True:
    seed = random.getrandbits(32)
    r = random.Random(seed)
    x = r.getrandbits(32)
    if x <= 10:
        print(seed)
        print(x)
        break
