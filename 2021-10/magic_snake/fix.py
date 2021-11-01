with open("magic.pyc", "rb") as f:
    data = bytearray(f.read())
data[0] = 0x55
with open("magic.fix.pyc", "wb") as f:
    f.write(data)

# decompyle3 magic.fix.pyc
# ictf{I_hope_this_one_wasn't_too_gue55y...}
