from base64 import *
import pyzipper

with pyzipper.AESZipFile("chall.zip") as zf:
    zf.setpassword(b64decode(b"ng3pV1YIws4l91Ai04m3IMVa2kg="))
    print(zf.read("ng3pV1YIws4l91Ai04m3IMVa2kg="))

# https://twitter.com/Unblvr1/status/1561112433812463616
# ictf{fastest_hash_cracking_gun_in_the_w3st}
