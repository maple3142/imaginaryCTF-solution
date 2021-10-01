from sage.all import primes_first_n, product

# fmt: off
keys = [0o152, 0o144, 0o153, 0o155, 0o160, 0o136, 0o73, 0o31, 0o43, 0o47, 0o51, 0o71, 0o124, 0o56, 0o170, 0o100, 0o41, 0o112, 0o132, 0o134, 0o145, 0o54, 0o133, 0o124, 0o44, 0o173, 0o177, 0o46, 0o155, 0o32, 0o154, 0o153, 0o72, 0o107, 0o154, 0o124, 0o41, 0o145, 0o161, 0o124, 0o32, 0o35, 0o132, 0o154, 0o166, 0o177, 0o73, 0o100, 0o176, 0o107, 0o161, 0o54, 0o155, 0o154, 0o177, 0o53, 0o173, 0o161, 0o166, 0o132, 0o46, 0o172, 0o140, 0o46, 0o145, 0o166, 0o46, 0o166, 0o161, 0o140, 0o146, 0o113, 0o54, 0o133, 0o52, 0o142]
# fmt: on

ps = primes_first_n(len(keys) + 1)
l = [1 + product(ps[:i]) for i in range(len(ps))][1:]

for k, t in zip(keys, l):
    print(chr(k ^ t % 50), end="")
