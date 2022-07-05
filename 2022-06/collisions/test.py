from requests import get
from zlib import crc32
from PIL import Image
from io import BytesIO

def compare_image(b):
    old_image = Image.open("orig_image.png")
    new_image = Image.open(BytesIO(b))
    return list(old_image.getdata()) == list(new_image.getdata())

print('='*80)
print(open(__file__).read())
print("="*80+'\n')

with open('new_image.png', 'rb') as f:
    image_bytes = f.read()

print(compare_image(image_bytes))
if crc32(image_bytes) == 0 and compare_image(image_bytes):
    print(open("flag.txt").read())
else:
    print("Better luck next time!")

