from Crypto.Cipher import AES

ct = b"\xd6\x19O\xbeA\xb0\x15\x87\x0e\xc7\xc4\xc1\xe9h\xd8\xe6\xc6\x95\x82\xaa#\x91\xdb2l\xfa\xf7\xe1C\xb8\x11\x04\x82p\xe5\x9e\xb1\x0c*\xcc[('\x0f\xcc\xa7W\xff"

for word in open("/home/maple3142/winhome/Downloads/rockyou.txt", "rb"):
    key = word.strip().zfill(16)
    cipher = AES.new(key, AES.MODE_ECB)
    flag = cipher.decrypt(ct)
    if b"ictf" in flag:
        print(word)
        print(flag)
        break
