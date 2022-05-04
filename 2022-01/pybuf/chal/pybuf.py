#!/usr/bin/env python3

import ctypes

c = ctypes.CDLL(None)
a = "asdf"
b = "bbbb"
c.write(1, ctypes.cast(id(a), ctypes.POINTER(ctypes.c_char)), 512)
c.gets(ctypes.cast(id(a), ctypes.POINTER(ctypes.c_char)))

if b == "flag":
  print(open("flag.txt").read())
