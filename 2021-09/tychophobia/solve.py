import hashlib

enc = b"\x1d\x80\x1d\xe0\xa7\x89\x9d\x0f3\xa03`z\x8d\x1b\xbc\xe4\xb7\xcec9\x7f\x8d\x00\xbf\xee\xb7\xc0>js\xafa"
key = enc[0] ^ ord("i")
flag = b""
for c in enc:
    flag += bytes([c ^ key])
    key = hashlib.md5(bytes([key])).digest()[0]
    if key == 0:
        key += 1
print(flag)
