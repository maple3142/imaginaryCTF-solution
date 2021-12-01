#!/usr/bin/env python3

target = b'YSDVKWUDoQoBUQ\\oB^Wo@\\CM'

def rand(seed):
  return eval(bytes([n^(eval(("0b10+"*21)[:-1])) for n in b'CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03']))

def jumble(n):
  return n*11 + rand(n)

def enc(c: bytes):
  return bytes([_^jumble(rand(42)) for _ in c])

def main():
  i = input("What is the flag? ").encode()
  if enc(i) == target:
    print("Correct!")
  else:
    print("Wrong.")

if __name__ == "__main__":
  main()
