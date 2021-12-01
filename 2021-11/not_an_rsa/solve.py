from Crypto.Util.number import bytes_to_long

ct = (
    b"\xf2\xa3\x91lT=\r\xed\x9c\x9ahS;\x10\xd8\x99\x85\x7fA\x05\r\xd7\xa8\xb1\x7fW1\xff"
)

a = ct[0] ^ ord("i")
aa = ct[1] ^ ord("c")
b = (aa - a) % 256

for c in ct:
    print(chr(c ^ a), end="")
    a = (a + b) % 256
