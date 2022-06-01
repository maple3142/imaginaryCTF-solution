#!/usr/bin/env python3

def validate(code, chars=[]):
    initial_len = len(chars)
    for char in code:
        if char not in chars:
            chars.append(char)
        if len(chars) - initial_len > 1:
            return False
    return True

print('='*80)
print(open(__file__).read())
print('='*80)

while True:
    declare = input("What characters would you like to use in your escape attempt?\n>>> ")
    chars = list(set(declare.strip()))
    code = input("Enter your command\n>>> ")
    if len(chars) > 3:
        valid = False
    elif len(chars) > 0:
        valid = validate(code, chars)
    else:
        valid = validate(code)
    if not valid:
        print("Command not accepted.")
        continue
    exec(code)
