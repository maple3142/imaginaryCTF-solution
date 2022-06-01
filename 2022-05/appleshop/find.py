from z3 import *

price = 1000000
cnt = BitVec("cnt", 32)
opt = Optimize()
opt.add(UDiv(cnt * price, price) == cnt)
opt.maximize(cnt)
opt.check()
print(opt.model()[cnt])
