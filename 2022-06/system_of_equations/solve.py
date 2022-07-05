import angr
import claripy
from capstone import *
from capstone.x86 import *
from pwn import *

elf = ELF("./challenge_8")
data = elf.read(elf.sym['main'], 0x1000)
md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
insts = list(md.disasm(data, elf.sym['main']))
avoids = []
for inst in insts:
    if inst.mnemonic == 'mov' and inst.op_str == 'dword ptr [rbp - 4], 0':
        avoids.append(inst.address + 0x400000)
        print(hex(inst.address))
        print(inst.op_str)

input_len = 24
flag_chars = [claripy.BVS("flag_%d" % i, 8) for i in range(input_len)]
flag = claripy.Concat(*flag_chars)

proj = angr.Project("./challenge_8")
st = proj.factory.entry_state(
    args=["./challenge_8", flag], add_options=angr.options.unicorn
)
for k in flag_chars:
    st.solver.add(k < 0x7F)
    st.solver.add(k > 0x20)

sm = proj.factory.simulation_manager(st)
sm.explore(avoid=avoids).unstash(from_stash='avoid', to_stash='active')
for s in sm.deadended:
    if b"CORRECT" in s.posix.dumps(1):
        flag =  bytes([s.solver.eval(x) for x in flag_chars])
        print(flag)
# ictf{class1c_aut0mati0n}
