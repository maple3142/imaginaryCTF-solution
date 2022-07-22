gdb.execute("gef config context.enable false")
gdb.execute('start < /dev/null')
flag = ''
while True:
    cur_inst = gdb.execute("x/i $pc",to_string=True)
    print(cur_inst)
    print(flag)
    # if 'mov    al,BYTE PTR [rsp]' in cur_inst:
    #     acc = 0
    # if 'sub    al,' in cur_inst:
    #     acc += int(cur_inst.split('sub    al,')[1].strip(), 16)
    if 'xor    BYTE PTR [rip+0x7],al' in cur_inst:
        val = 256 - int(str(gdb.parse_and_eval("$al")), 16)
        flag += chr(val)
        gdb.execute('set $al = 0')
        # break
    gdb.execute('si')
# gdb ./polymorphic -x solve.py
# ictf{dynam1c_d3bugg1ng_1s_n1ce}
