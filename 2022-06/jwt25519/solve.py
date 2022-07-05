import requests
from base64 import b64decode, b64encode
import json
from ed25519 import signature, publickey, checkvalid

SECRET_KEY = b"pekomiko"
PUB = b64encode(publickey(SECRET_KEY)).decode()
print(PUB)


def b64pad(b):
    while len(b) % 4 != 0:
        b += b"="
    return b


class JWT:
    def __init__(self, data):
        self.header = {
            "alg": "ED25519",
            "typ": "JWT",
            "public_key": b64encode(publickey(SECRET_KEY)).decode(),
            **data,
        }
        self.header_bytes = b64encode(json.dumps(self.header).encode()).replace(
            b"=", b""
        )
        self.data = {**data}
        self.data_bytes = b64encode(json.dumps(self.data).encode()).replace(b"=", b"")
        self.signature = signature(
            self.data_bytes, SECRET_KEY, b64decode(self.header["public_key"].encode())
        )
        self.signature_bytes = b64encode(self.signature).replace(b"=", b"")

    def validate(self):
        try:
            checkvalid(
                self.signature,
                self.data_bytes,
                b64decode(self.header["public_key"].encode()),
            )
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def from_str(cls, s):
        ret = cls({})
        ret.header_bytes, ret.data_bytes, ret.signature_bytes = s.encode().split(b".")
        header_bytes = b64pad(ret.header_bytes)
        data_bytes = b64pad(ret.data_bytes)
        signature_bytes = b64pad(ret.signature_bytes)

        ret.header = json.loads(b64decode(header_bytes).decode())
        ret.data = json.loads(b64decode(data_bytes).decode())
        ret.signature = b64decode(signature_bytes)

        return ret

    def __str__(self):
        return b".".join(
            [self.header_bytes, self.data_bytes, self.signature_bytes]
        ).decode()


jwt = str(JWT({"username": "admin", "password": "password"}))
r = requests.get(
    "http://puzzler7.imaginaryctf.org:2999/flag",
    cookies={"token": jwt},
    allow_redirects=False,
)
print(r.text)
# ictf{don't_worry_I_won't_put_you_through_any_more_side_channel_attacks...for_now}
# Intended: https://github.com/MystenLabs/ed25519-unsafe-libs


# r = requests.post('http://puzzler7.imaginaryctf.org:2999/login',json={
#     'username': 'admin',
#     'public_key': PUB
# }, allow_redirects=False)
# jwt = r.headers['set-cookie'].split('=',1)[1].split(';')[0]
# print(jwt)
# hdr, data, sig = jwt.split('.')
# print(b64decode(hdr + '=='))
# print(b64decode(data + '=='))
# print(JWT.from_str(jwt).validate())
