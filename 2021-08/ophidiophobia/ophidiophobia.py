#!/usr/bin/env python3

import ctypes
import unicodedata

i = unicodedata.normalize("NFKC", input(">>> "))

assert not any([n in i for n in ["_"]])
assert len(i) <= 50

eval(i, {"ctypes": ctypes, "__builtins__": {}})
