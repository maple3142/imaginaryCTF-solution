from z3 import *

flag = [BitVec(f"f_{i}", 32) for i in range(28)]
# sol = Solver()
set_param("parallel.enable", True)
set_param("parallel.threads.max", 12)
sol = SolverFor("QF_BV")  # It is said to be faster for fixed sized bitvectors

A = 0
B = 0
u = 0
for c in flag:
    sol.add(Or([c == x for x in b"ZYPH3NAFUR1GT_BMKLE.0"]))
    A += c
    B ^= c
    # u = (u << 5) - u + c
    u = 31 * u + c


def floor_div(top, bottom, res):
    # floor(top / bottom) == res
    sol.add(top >= bottom * res)
    sol.add(top < bottom * res + bottom)


sol.add(A == 2024)
sol.add(B == 126)
sol.add(u == BitVecVal(-685590366, 32))
sol.add(1 == flag[0] - flag[1])
# sol.add(277 == flag[1] * flag[2] * flag[3] / 1846)
floor_div(flag[1] * flag[2] * flag[3], 1846, 277)
sol.add(114 == flag[4] + flag[5] - flag[6] + flag[7])
# sol.add(3249 == ((flag[8] * flag[9]) / flag[10]) * flag[11])
floor_div(flag[8] * flag[9] * flag[11], flag[10], 3249)
# sol.add(1 == flag[13] / flag[12] / flag[14] * flag[15])
floor_div(flag[13] * flag[15], flag[12] * flag[14], 1)
sol.add(flag[18] == len("ZYPH3NAFUR1GT_BMKLE.0") << 2)
sol.add(flag[6] == flag[17])
# sol.add(46 == flag[19] * flag[20] / flag[21])
floor_div(flag[19] * flag[20], flag[21], 46)
sol.add(116 == flag[22] + flag[23] - flag[24])
sol.add(138 == flag[25] + flag[26] + flag[27])

# Some burteforcing to make the search space smaller: https://wrecktheline.com/writeups/imaginary-2021/

sol.add(flag[27] == ord("."))
sol.add(flag[26] == ord("."))
sol.add(flag[25] == ord("."))
sol.add(flag[24] == ord("3"))
sol.add(flag[23] == ord("R"))
sol.add(flag[22] == ord("U"))
sol.add(flag[21] == ord("T"))
sol.add(flag[20] == ord("R"))
sol.add(flag[19] == ord("0"))
sol.add(flag[18] == ord("T"))
sol.add(flag[17] == ord("_"))

sol.add(flag[0] == ord("Z"))
sol.add(flag[1] == ord("Y"))
sol.add(flag[2] == ord("P"))
sol.add(flag[3] == ord("H"))
sol.add(flag[4] == ord("3"))
sol.add(flag[5] == ord("N"))
sol.add(flag[6] == ord("_"))
sol.add(flag[7] == ord("P"))

print("solving...")

assert sol.check() == sat

while sol.check() == sat:
    m = sol.model()
    ans = bytes([m[x].as_long() for x in flag])
    print(ans)
    sol.add(Or([a != b for a, b in zip(ans, flag)]))
