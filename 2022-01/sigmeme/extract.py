from pwn import *

elf = ELF("./sig")
index_ar = list(elf.read(0x4AE0F0, 28))
target_ar = list(elf.read(0x482040, 55))
print(index_ar)
print(target_ar)
