#!/usr/bin/env python3

from random import randint, choice
from time import time

# https://pypi.org/project/console/
from console.utils import wait_key
from console.screen import Screen

def win():
    print(screen.clear, end='')
    with screen.location(0, 0):
        print(f"Great job! {open('flag.txt').read()}")

    with screen.location(2, 0):
        print("Press any key to exit.")

    wait_key()
    exit(0)

def die(msg="Sorry, that's not correct."):
    print(screen.clear, end='')
    with screen.location(0, 0):
        print(msg)

    with screen.location(2, 0):
        print("Press any key to exit.")

    wait_key()
    exit(0)

def draw(n1, n2, op):
    eq = "%d %s %d = ?"%(n1, op, n2)
    ans = eval(eq[:-3])
    y = randint(1, 18)
    x = randint(1, 79-len(eq)-1)

    print(screen.clear, end='')
    for row in range(20):
        with screen.location(row, 0):
            if row == 0:
                print('╔' + '═'*78 + '╗', end='')
            elif row == 19:
                print('╚' + '═'*78 + '╝', end='')
            else:
                print('║' + ' '*78 + '║', end='')
                if row == y:
                    with screen.location(y, x):
                        print(eq, end='')

    with screen.location(22, 0):
        print(" "*80)
    with screen.location(22, 0):
        user_ans = int(input(">>> "))

    return ans == user_ans


def main():
    with screen.fullscreen():
        start = time()
        for i in range(100):
            n1 = randint(10000, 99999)
            n2 = randint(10000, 99999)
            op = choice('*-+^&|')
            if not draw(n1, n2, op):
                die()
            if time() - start > 100:
                die("Out of time!")
        win()

if __name__ == '__main__':
    with Screen(force=True) as screen:
        main()