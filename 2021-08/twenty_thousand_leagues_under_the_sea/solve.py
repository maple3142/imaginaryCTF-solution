from pwn import process, remote

with open("TwentyThousandWordlist.txt") as word_list:
    # from https://www.gutenberg.org/files/164/164-h/164-h.htm
    words = word_list.read().split()


def find_popular_prefix(words, n, k):
    dt = {}
    for w in words:
        pfx = w[:n]
        if pfx not in dt:
            dt[pfx] = 0
        dt[pfx] += 1
    return sorted(dt.items(), key=lambda e: e[1], reverse=True)[k][0]


def attempt():
    traced = set(words)
    pfx = ""
    # io = process(["python", "server.py"])
    io = remote("puzzler7.imaginaryctf.org", 9000)
    io.recvuntil("Ready?")
    k = 0
    for i in range(20):
        io.recvuntil(b"guess")
        io.recvline()
        if len(traced) == 1:
            print(next(iter(traced)))
            io.sendline(next(iter(traced)))
            break
        p = find_popular_prefix(traced, len(pfx) + 1, k)
        io.sendline("^" + p)
        if "Yes" in io.recvlineS():
            pfx = p
            k = 0
            traced = set(x for x in traced if x.startswith(pfx))
        else:
            k += 1
        print(i, p, pfx)

    r = io.recvallS()
    print(r)
    if "Correct" in r:
        exit()


while True:
    attempt()
