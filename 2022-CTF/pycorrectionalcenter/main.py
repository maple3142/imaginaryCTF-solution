#!/usr/bin/env python3.9

trash = {}

def main():
  print("Welcome to the Python Correctional Center, where you won't be able to escape!")
  allowed_variables = {**vars(__builtins__).copy(), **globals()}
  for name in ["exec", "eval", "__import__", "breakpoint", "input", "__builtins__", "getattr", "setattr", "delattr", "license", "vars"]:
    allowed_variables[name] = None
  inp = input(">>> ")
  assert all([ord(c) < 128 for c in inp])
  assert not '.' in inp
  assert not '_' in inp
  assert not '!' in inp
  assert not '*' in inp
  assert not '&' in inp
  assert not '@' in inp
  assert not '`' in inp
  assert not '~' in inp
  assert not '{' in inp
  assert not '}' in inp
  # assert not ';' in inp
  assert not '\'' in inp
  assert not '\'' in inp
  assert not 'lambda' in inp
  assert not 'raise' in inp
  assert not 'assert' in inp
  assert not 'if' in inp
  assert not 'for' in inp
  assert not 'import' in inp
  assert len(inp) < 12
  exec(inp, {"__builtins__": allowed_variables}, trash)
  exit()

if __name__ == "__main__":
  main()
