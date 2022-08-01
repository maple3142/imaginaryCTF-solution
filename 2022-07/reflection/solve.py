import angr
import claripy
from capstone import *
from capstone.x86 import *
from pwn import *

input_len = 65
flag_chars = [claripy.BVS("flag_%d" % i, 8) for i in range(input_len)]
flag = claripy.Concat(*flag_chars)

proj = angr.Project("./reflection")
st = proj.factory.entry_state(
    args=["./reflection"], add_options=angr.options.unicorn, stdin=flag
)
for k in flag_chars:
    st.solver.add(k < 0x7F)
    st.solver.add(k > 0x20)

sm = proj.factory.simulation_manager(st)
sm.run()
for s in sm.deadended:
    if b"yes" in s.posix.dumps(1):
        flag = bytes([s.solver.eval(x) for x in flag_chars])
        print(flag.decode())
