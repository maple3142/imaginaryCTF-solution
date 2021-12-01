import angr
import claripy

input_len = 3
flag_chars = [claripy.BVS("flag_%d" % i, 8) for i in range(input_len)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b"\n")])

proj = angr.Project("./bf")
st = proj.factory.full_init_state(
    args=["./bf"], add_options=angr.options.unicorn, stdin=flag
)
for k in flag_chars:
    st.solver.add(k < 0x7F)
    st.solver.add(k > 0x20)

sm = proj.factory.simulation_manager(st)
sm.run()
y = []
for x in sm.deadended:
    if b"right" in x.posix.dumps(1):
        y.append(x)
valid = y[0].posix.dumps(0)
print(valid)
bt = [chr(valid[i]) for i in range(0, len(valid))]
print("".join(bt))
