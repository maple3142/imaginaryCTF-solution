from PIL import Image

img = Image.open("colors.png").convert("RGB")

dx = img.width // 14
x = dx // 2
y = img.height // 2
while x < img.width:
    r, g, b = img.getpixel((x, y))
    print(chr(r) + chr(g) + chr(b), end="")
    x += dx
