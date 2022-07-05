with open("output.txt") as f:
    s = f.read().strip()


def xx(n):
    r = n - shift if n - shift < 30 else n - shift - 128
    return r + 97


shift = 18
flag = ""
for c in s:
    n = ord(c) - 97
    print(n, n - shift)
    flag += chr(xx(n))
    shift = ((n + 32) * 1337) % 27
print(flag)

shift = 18
res = ""

for n in flag:
    n = ord(n) - 97
    n = (n + shift) % 128
    res += chr(n + 97)
    shift = ((n + 32) * 1337) % 27
print(res)
print(res == s)
