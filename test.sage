F = GF(2)
n = 40

P.<x> = F[]

v = random_vector(F, n)
v = vector([F(1)]*n)
M = companion_matrix(1 + x + x^5 + x^8+x ^ n, 'bottom')
u = M ^ 87 * v
print(v)
print(u)

vs = [M ^ (2 ^ i) * v for i in range(n)]

print(matrix(vs).rank())

r=matrix(vs).solve_left(u)
assert r*matrix(vs)==vector(u)
print(r)
r=matrix(vs).solve_left(u-v)
assert r*matrix(vs)==vector(u-v)
print(r)
print(bin(87))
