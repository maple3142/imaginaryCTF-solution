import string
import sys

b64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
assert len(b64) == 64

def decode_to_bits(s):
    bits = ''
    for c in s:
        v = b64.index(c)
        bits += f'{v:06b}'
    return bits

print(decode_to_bits(sys.argv[1]))
