from chal import n, e
import secrets, hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

if __name__ == "__main__":
    with open("flag.txt", "rb") as f:
        flag = f.read().strip()

    k = secrets.randbelow(n)
    print(f"{pow(k, e, n) = }")
    key = hashlib.sha256(hex(k).encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    print(f"{cipher.encrypt(pad(flag, 16)).hex() = }")

    while True:
        p = int(input())
        assert p >= 0
        print(pow(p, e, n))
