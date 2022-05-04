with open("firmware.hex") as f:
    for line in f:
        print(bytes.fromhex(line[1:]))
