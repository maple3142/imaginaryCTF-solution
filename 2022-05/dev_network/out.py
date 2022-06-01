data = b""
with open("dump") as f:
    for line in f:
        data += bytes.fromhex(line)
with open("proj_test", "wb") as f:
    f.write(data)

# open IDA and found it is flag xor with 1
# ictf{M@k3_$ur3_T0_u$3_t1s_f0r_ftp}
