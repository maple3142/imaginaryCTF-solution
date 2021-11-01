with open("puzzle.txt") as f:
    print("ictf{" + "".join(l[0] for l in f) + "}")
