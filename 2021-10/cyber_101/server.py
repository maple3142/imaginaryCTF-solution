import time
from flag import flag
from random import randint

amount = 100
print(f"Hello and welcome to an epic math battle. ok so I will send you {amount} of problems and you need to solve it in under 60 seconds. Ok Go!")
start_time = time.time()
for i in range(amount): 
    if time.time() - start_time >= 60:
        break
    x, y = randint(0, 10), randint(0, 10)
    if randint(0, 1) == 0:
        print(f"{x} + {y}")
        ans = x + y
    else:
        print(f"{x} - {y}")
        ans = x - y

    user_ans = int(input())
    if user_ans != ans:
        print("That was incorect, goodbye")
        exit()
else:
    print(f"Impresive, here is your flag: {flag}")
    print("if your are able to do this by hand, please dm me a video of it. i really want to see.")
    exit()

print("Times Up, Try Again Later")