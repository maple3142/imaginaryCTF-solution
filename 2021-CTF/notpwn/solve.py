import angr
import claripy

input_len = 16
stdin_chars = [claripy.BVS("stdin_%d" % i, 8) for i in range(input_len)]
stdin = claripy.Concat(
    *[claripy.BVV(b"a") for _ in range(10)] + stdin_chars + [claripy.BVV(b"\n")]
)

proj = angr.Project("./notpwn")
st = proj.factory.entry_state(args=["./notpwn"], stdin=stdin)
for k in stdin_chars:
    st.solver.add(k < 0x7F)
    st.solver.add(k > 0x20)

sm = proj.factory.simulation_manager(st)
# this part isn't necessary...
# # enter fake __stack_chk_fail
# sm.explore(find=0x4011B5).unstash(from_stash="found", to_stash="active")
# # loop 0
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# sm.explore(find=0x401377).unstash(from_stash="found", to_stash="active")
# # loop 1
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# sm.explore(find=0x401377).unstash(from_stash="found", to_stash="active")
# # loop 2
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# sm.explore(find=0x401377).unstash(from_stash="found", to_stash="active")
# # loop 3
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# sm.explore(find=0x401377).unstash(from_stash="found", to_stash="active")
# # loop 4
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# sm.explore(find=0x401377).unstash(from_stash="found", to_stash="active")
# # loop 5
# sm.explore(find=0x40136F, avoid=0x40130C).unstash(from_stash="found", to_stash="active")
# exit
# end of fake __stack_chk_fail
sm.explore(find=0x40137E)
print("stdin", sm.found[0].posix.dumps(0))
print("stdout", sm.found[0].posix.dumps(1))
