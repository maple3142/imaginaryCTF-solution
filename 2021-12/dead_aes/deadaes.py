#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Util.Padding import pad
from random import getrandbits

def gen():
	# weird order of operations or whatever
	# but make sure to separate the x<<n from other stuff with parentheses
	a = getrandbits(32)
	b = getrandbits(32)
	c = getrandbits(32)
	d = getrandbits(32)
	return (a<<96)+(b<<64)+(c<<32)+(d)

# AES-128
if __name__ == '__main__':
	print("Partially an AES challenge")
	while True:
		print()
		print("="*80)
		print()
		print("(E)ncrypt")
		print("(R)equest encrypted flag")
		print("(L)eave")
		print()
		option = input("Enter your option: ").lower()
		if option == "e":
			pt = input("Enter your message: ").encode()
			# 128 bits = 16 bytes
			# our blocks are 16 byte sized
			pt = pad(pt, 16)
			key = gen()
			iv = gen()
			key = ltb(key).rjust(16, b"\x00")
			iv = ltb(iv).rjust(16, b"\x00")
			
			c = AES.new(key, AES.MODE_CBC, iv=iv)
			ct = c.encrypt(pt)
			
			iv = b"never gonna give you up"
			
			print()
			a = f"Your ciphertext (hex) is {ct.hex()}."
			b = f"Your key (hex) is {key.hex()}."
			c = "Unfortunately, the IV got corrupted, so I can't give it :("
			plen = max(len(a), len(b), len(c))
			print("="*plen)
			print(a)
			print(b)
			print(c)
			print("="*plen)
			print("\nSuccess!")
		elif option == "r":
			flag = open("flag.txt", "rb").read()
			pt = pad(flag, 16)
			key = gen()
			iv = gen()
			key = ltb(key)
			iv = ltb(iv)
			
			c = AES.new(key, AES.MODE_CBC, iv=iv)
			ct = c.encrypt(pt)
			
			key = b"never gonna give you up"
			
			print()
			a = f"Your encrypted flag (hex) is {ct.hex()}."
			b = f"Your IV (hex) is {iv.hex()}."
			c = "Unfortunately, the key got corrupted, so I can't give it :("
			plen = max(len(a), len(b), len(c))
			print("="*plen)
			print(a)
			print(b)
			print(c)
			print("="*plen)
			print("\nSuccess!")
		elif option == "l":
			exit(0)
		else:
			print("Invalid option")



