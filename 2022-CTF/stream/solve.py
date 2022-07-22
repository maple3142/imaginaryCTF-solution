with open("out.txt", "rb") as f:
    ct = f.read()


def decrypt(ct, key):
    pt = b""
    for i in range(0, len(ct), 8):
        x = int.from_bytes(ct[i : i + 8], "little")
        x ^= key
        pt += x.to_bytes(8, "little")
        key = (key * key) & 0xFFFFFFFFFFFFFFFF
    return pt[: len(ct)]


key = int.from_bytes(b"ictf{\x00\x00\x00", "little") ^ int.from_bytes(ct[:8], "little")
key &= ~0xFFFFFF0000000000
for i in range(256**3):
    k = key + (i << 40)
    f = decrypt(ct, k).strip(b"\n\x00")
    if f.startswith(b"ictf{") and f.endswith(b"}") and f.isascii():
        print(f)
        break
# pypy3 solve.py
# ictf{y0u_rec0vered_my_keystream_901bf2e4}
