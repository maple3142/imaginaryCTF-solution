from autocorrect import Speller

spell = Speller(lang="en")

with open("words.txt") as f:
    words = [x.strip() for x in f.readlines()]


def diff(a, b):
    for x, y in zip(a, b):
        if x != y:
            return x


for w in words:
    if w != spell(w):
        print(diff(w, spell(w)), end="")
