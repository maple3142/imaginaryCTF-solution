import sys

keys = [0o152, 0o144, 0o153, 0o155, 0o160, 0o136, 0o73, 0o31, 0o43, 0o47, 0o51, 0o71, 0o124, 0o56, 0o170, 0o100, 0o41, 0o112, 0o132, 0o134, 0o145, 0o54, 0o133, 0o124, 0o44, 0o173, 0o177, 0o46, 0o155, 0o32, 0o154, 0o153, 0o72, 0o107, 0o154, 0o124, 0o41, 0o145, 0o161, 0o124, 0o32, 0o35, 0o132, 0o154, 0o166, 0o177, 0o73, 0o100, 0o176, 0o107, 0o161, 0o54, 0o155, 0o154, 0o177, 0o53, 0o173, 0o161, 0o166, 0o132, 0o46, 0o172, 0o140, 0o46, 0o145, 0o166, 0o46, 0o166, 0o161, 0o140, 0o146, 0o113, 0o54, 0o133, 0o52, 0o142]

i = 2
l = []
for k in keys:
  while True:
    if((lambda f: lambda g: lambda *h: g(f(lambda g: f(g))(g))(*h))(lambda h: lambda f: lambda *g: f(h(lambda g: h(g))(f))(*g))((lambda g: lambda f: lambda h,i=2: [lambda: True, lambda: g((h % i) * f(h, i+1))][1 - (i >= h)]())(type(... is not None)))(i)):
      l.append(i)
      p = not (r := 1) or [r := r*a for a in l][-1]
      if(not (lambda n: all([False for i in range(2,n) if n % i == 0 ]) and not n < 2)(p) or p < 3):
        t = (lambda *g: sum(g))(p, 1)
        if(not t ** 0.5 + 0.5 ** 2 == t):
          sys.stdout.write(chr(k^t % 50))
          sys.stdout.flush()
      i += 1
      break
    else:
      i += 1
else:
  print()

# Credits to Robin_Jadoul for an amazing code snippet!
