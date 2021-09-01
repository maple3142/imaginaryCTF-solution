import ctypes

print(ctypes.string_at(id(0) + 16,100))
# print(hex(int.from_bytes(ctypes.string_at(id(ctypes) + 16,8),'little')))
# print(hex(int.from_bytes(ctypes.string_at(id(ctypes) + 42,8),'little')))
input()
