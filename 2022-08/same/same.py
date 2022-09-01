from Crypto.Util.number import getPrime, bytes_to_long
m = bytes_to_long(open("flag", "rb").read())
n = getPrime(512)*getPrime(512)
e = [1337,31337]
print(n)
print(pow(m,e[0],n))
print(pow(m,e[1],n))
