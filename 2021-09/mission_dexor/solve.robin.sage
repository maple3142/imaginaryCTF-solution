from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import itertools

F = GF(2)
tobin = lambda x: vector(F, "".join(f"{i:08b}" for i in x))
xor = lambda x, y: [x + y for x, y in zip(x, itertools.cycle(y))]
shift = lambda v: vector([*v[-1:], *v[:-1]])

bits = tobin(bytes.fromhex("bdabad262e769d0406e0bd299850a84f57775854f7811b2235ce800d780683075773"))
R = F[",".join(f"i_{i}" for i in range(len(bits)))]
flag = R.gens()
vars = R.gens()

password = tobin(b"g1v3fl4g")
rounds = 5

for u in range(rounds):
    s = shift(flag)
    n = xor(s, password)
    flag = xor(flag, n)

M = Matrix([[f.monomial_coefficient(i) for i in vars] + [f.constant_coefficient()] for f in flag])
sol0 = M \ bits
kern = Matrix(M.right_kernel().basis())

for z in itertools.product([0, 1], repeat=kern.dimensions()[0]):
    sol = sol0 + vector(F, z) * kern
    assert M * sol == bits
    x = ltb(int(''.join(map(str, sol[:-1])), 2))
    if x.startswith(b"ictf{"):
        print(x.decode())
