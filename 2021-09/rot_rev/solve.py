import string

T1 = str.maketrans(
    string.ascii_lowercase, string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
)
T2 = str.maketrans(
    string.ascii_uppercase, string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
)

with open("rotversing.py") as f:
    s = f.read()

print(s.translate(T1).translate(T2))

from base64 import b64decode

d = b"YVdOMFpudGxibU13WkRGdVoxOHhjMTl1TUhSZlpXNWpjbmx3ZERFd2JuMD0="
print(b64decode(b64decode(d)))
