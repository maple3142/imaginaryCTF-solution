with open("mem.bin", "rb") as f:
    # use gdb to dump entire process memory after rooScientist completes
    mem = f.read()
    rop = mem[0x4840:]
    chain = [int.from_bytes(rop[i : i + 8], "little") for i in range(0, len(rop), 8)]

rop_map = {
    0x401141: "pop rdi",
    0x401143: "pop rsi",
    0x40114D: "mov QWORD PTR [rsi], rdi",
    0x40114B: "pop rax",
    0x40113E: "syscall",
    0x401151: "cmp; cmovz",
    0x40115D: "mov rsi, rcx",
    0x401161: "mov rdi, rdx",
    0x401159: "movzx ecx, BYTE PTR [rdx]",
    0x401145: "pop rdx",
}

base = 0x40406A  # input memory address

flag = [None] * 0x40

for i, r in enumerate(chain):
    if r == 0x573F573F573F573F:
        break
    if r in rop_map:
        print(rop_map[r])
    elif hex(r).startswith("0x40") and r >= 0x400000:
        print(hex(r))
        print(">", chr(mem[r - 0x400000]))
        if chain[i + 2] == 0x40115D:  # mov rsi, rcx
            fc = chr(mem[r - 0x400000])
            offset = chain[i + 4] - base
            print("=" * 8, offset, fc)
            flag[offset] = fc
    else:
        print(hex(r))

flag = flag[: flag.index(None)]
print("".join(flag))
