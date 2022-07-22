with open("flag.txt", "rb") as f:
    for x in f.read():
        assert (0x20 <= x and x <= 0x7F) or (x == 0x0A), bytes([x])
