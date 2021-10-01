from PIL import Image
from random import randint

with open("flag.bin", "rb") as f:
    data = f.read()


def randcolor():
    return randint(0, 255), randint(0, 255), randint(0, 255)


colormap = {}
chunks = list(zip(*[iter(data)] * 16))
img = Image.new("RGB", (1000, 50))
for x in range(1000):
    for y in range(50):
        chk = chunks[y * 1000 + x]
        if chk not in colormap:
            colormap[chk] = randcolor()
        rgb = colormap[chk]
        img.putpixel((x, y), rgb)
img.save("flag.png")

# another cool solution: https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'19c0%206958%203b22%20f010%201471%204aef%20daf6%208652'%7D,'Standard',false)Generate_Image('RGBA',1,1000)
