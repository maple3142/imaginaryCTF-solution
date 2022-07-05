from pwn import bits

with open("encoded.huff", "rb") as f:
    huffman = {}
    while True:
        t = f.read(3)
        if t == b"\0\0\0":
            break
        val = t[0]
        idx = int.from_bytes(t[1:], "big")
        huffman[idx] = val
        # print(val, bin(idx))
    bs = bits(f.read())
    c = 0
    for b in bs:
        c = (c << 1) | b
        if c in huffman:
            print(chr(huffman[c]), end="")
            c = 0
# ictf{I_stayed_up_entirely_too_late_debugging_this_stupid_thing_I_hope_it_actually_works}
