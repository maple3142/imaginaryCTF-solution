s = b":4E7L>J08:7E0E@0J@F0:D0E9:D0i02?@E96C062DJ0492==N"

mp = {}
for i in range(32, 128):
    mp[(i + 15) % 94 + 32] = i

print(bytes(mp[x] for x in s))
