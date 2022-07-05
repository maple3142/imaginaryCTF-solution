from datetime import *
import time
import random

flag = open("flag.txt", "r")
flag = flag.readline()
countdownStartTime = 1655500713
countdownLength = 000000000000000000000000 #in seconds (REDACTED)
timeLeft = countdownLength - (round(time.time())-countdownStartTime)

guess = int(input("How much seconds are left in my countdown?: "))
if guess < timeLeft:
    print("What kind of countdown do you think I'm running? A 2 second one?")
elif guess > timeLeft:
    print("Woah, I'm not holding a countdown until humans are extinct.")
else:
    print(f"Right on, here's your flag!: {flag}")
