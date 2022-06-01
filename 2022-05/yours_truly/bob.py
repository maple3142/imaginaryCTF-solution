from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from random import randint
from hashlib import md5

from signer import sign, get_verified_data

def die():
    print("Something's not right here...")
    exit()

gpa_signed = input("What did Alice say? ")
gpa_data = get_verified_data(gpa_signed)
if gpa_data is None:
    die()
sig, g, p, ga = gpa_data.decode().split(' ')[-4:]
if sig != "fromalice":
    die()
g = int(g)
p = int(p)
ga = int(ga)

b = randint(2, p-1)
b_signed = sign(('frombob '+str(pow(g, b, p))).encode()).decode()
print("Thanks! Tell her this:")
print(b_signed)

s = pow(ga, b, p)
key = md5(str(s).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)

message = input("What's her secret message? ")
msg_data = get_verified_data(message)
if msg_data is None:
    die()
flag = unpad(cipher.decrypt(msg_data), 16)

print("This is a great flag! Thank you for passing it along. Unfortunately, I can't share it with you though...")
print("Alice's message has made me a bit paranoid. I'm sure you understand.")
