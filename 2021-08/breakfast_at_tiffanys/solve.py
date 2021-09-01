with open("Breakfast_at_Tiffanys.v2.png", "rb") as f:
    data = f.read()

with open("output.tiff", "wb") as f:
    idxs = [0xE9F0, 0x9D61, 0x50D2, 0x447]
    for i in idxs:
        ln = int.from_bytes(data[i - 4 : i], "big")
        f.write(data[i + 4 : i + 4 + ln])

# ictf{Wh3n_1n_d0ub7_br0wse_7h3_b1n4ry}
