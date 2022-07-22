#!/usr/bin/env python3

import sys
import string

allowed = string.whitespace + string.ascii_lowercase
for name in sys.modules.keys():
  if any(n in name for n in ["heap", "imp", "marshal", "code", "func", "enc", "lib", "abc", "warn", ".", "x", "builtins"]):
    sys.modules[name] = None
del sys
del string

print("Welcome to the Python Crib. We honestly don't care if you escape.")
inp = input(">>> ")
b = not all([n in allowed for n in inp])
exec(inp) if not b else print("How cute!")
exit(b)
