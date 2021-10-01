import string

gdb.execute("gef config context.enable false")
gdb.execute("set print inferior-events off")
gdb.execute("b *(main+0x28b)")


def get_same(flag):
    gdb.execute(f'r "{flag}"')
    # gdb.execute("hexdump byte $rdi")
    # gdb.execute("hexdump byte $rsi")
    rdi = gdb.parse_and_eval("$rdi")
    rsi = gdb.parse_and_eval("$rsi")
    i = gdb.inferiors()[0]
    res = i.read_memory(rdi, 34).tobytes()
    exp = i.read_memory(rsi, 34).tobytes()
    same = len([1 for a, b in zip(res, exp) if a == b])
    return same


chs = (
    "{_}" + string.digits + string.ascii_lowercase + string.punctuation.replace('"', "")
)
flag = bytearray(b"ictf******************************")
for i in range(4, 34):
    cur = get_same(flag.decode())
    for c in chs:
        flag[i] = ord(c)
        if get_same(flag.decode()) > cur:
            break
    print(flag)

# run this script with gdb + gef
# gdb telephone -x solve.py
# ictf{y0u_c@nt_s7op_th3_s1gn@l_m@l}
