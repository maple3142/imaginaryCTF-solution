import random, itertools, collections, tqdm, hashlib, string, math

with open("out.txt") as f:
    ref = ''.join(x for x in f.read().lower() if x in string.ascii_lowercase)

def frequencies(X):
    K = 2
    freq = collections.Counter(zip(*[X[i:] for i in range(K)]))
    tot = len(X) - K
    # Log-space frequencies, unlabeled distribution represented as ordered list of frequencies
    res = sorted((math.log(v/tot) for v in freq.values()), reverse=True)
    return res
freq = frequencies(ref)

def score(t):
    # Alternatively, a bigram variant of the Index of Coincidence might give better results
    t = t[0]
    F = frequencies(t)
    return sum(abs(x - y) for x, y in zip(F, freq)) / len(F)

def unshuffle(seed):
    random.seed(seed)
    p = list(shuf)
    for i, j in [(i, random.randint(0, i)) for i in range(len(shuf) - 1, -1, -1)][::-1]:
        p[i], p[j] = p[j], p[i]
    return ''.join(p), seed

with open("out.txt") as f:
    shuf = f.read()

res, seed = min((unshuffle(bytes(s)) for s in tqdm.tqdm(itertools.product(range(256), repeat=2), total=256**2)), key=score)
print(seed)
print(res)
plain = ''.join(x for x in input("What does quipqiup say about this? ").lower() if x in string.ascii_lowercase)
d = {k:v for k, v in zip(plain, res)}
d[list(set(string.ascii_lowercase) - set(d.keys()))[0]] = list(set(string.ascii_lowercase) - set(d.values()))[0]
print(f"ictf{{{''.join(v for k, v in sorted(d.items()))}{bytes(seed).hex()}}}")
