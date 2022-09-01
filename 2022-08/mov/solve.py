from subprocess import Popen, PIPE


def get_cnt(flag):
    p = Popen([b"strace", b"./chall", flag], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return err.count(b"SIGSEGV")


flag = bytearray(b"ictf{xxxxxxxxxxxxxxxxxxxxxxx}")
for i in range(5, len(flag)):
    mx, mxc = -1, -1
    for j in range(1, 256):
        flag[i] = j
        c = get_cnt(bytes(flag))
        if c > mx:
            mx, mxc = c, j
    flag[i] = mxc
    print(flag)
# ictf{mov_S1d3_ChanN3l_Att4ck}
