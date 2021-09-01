from Crypto.Util.Padding import pad

# ImaginaryCTFUser idk
# Eth007 supersecure
# just_a_normal_user password
# firepwny pwned


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


username = b"firepwny"
token = bytes.fromhex("2023f20686ddab50dd0491b4861ad8bfaf5713f665fab499")
nonce, data = token[:8], token[8:]
key = xor(data, pad(username, 16))
newdata = xor(key, pad(b"admin", 16))
newtoken = nonce + newdata
print(newtoken.hex())
