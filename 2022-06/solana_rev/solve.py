# compile https://github.com/Toizi/eBPF-for-Ghidra then load it in ghidra
# or just read `llvm-objdump -D ./main.o`

data = b"\x07\x07\x00\x00\x0d\x47\x11\x0e\x39\x0e\x18\x74\x08\x0b\x17\x06\x6f\x5a\x44\x04\x00\x51\x07\x05\x45\x01\x00"
s = b"never gonna give you up never gonna let you down"
flag = bytes([x ^ i ^ s[i] for i, x in enumerate(data)])
print(flag)

# ictf{bpf_is_cool_29b41a23}
