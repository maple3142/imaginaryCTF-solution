flag = open("flag.txt", "r")
flag = flag.readline().strip()

shift = 18
res = ""

for n in flag:
   n = ord(n)-97
   n = (n+shift)%128
   res += chr(n+97)
   shift = ((n+32)*1337)%27

print(res)
