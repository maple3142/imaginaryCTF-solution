import random
import string

flag = open("flag.txt", "r").readline()
char_set = string.ascii_uppercase + string.digits

print("""                         .-. .-.
                        (   |   )
                      .-.:  |  ;,-.
                     (_ __`.|.'_ __)
                     (    ./Y\.    )
                      `-.-' | `-.-'
                            |
                            |      """)
print("\nTry your luck at guessing my passwords!")
print("A lucky number may help guide you in your guess...\n")

for n in range(200):
    chars = ''.join(random.sample(char_set*6, 6))
    key = ""
    for x in chars:
        key += str(ord(x))
    key = int(key)^1337
    key = ++key
    key = --key
    key = key - 10000000000
    print(f"Your lucky number is: {key}")
    user_answer = input("What's my password? ")
    if user_answer == chars:
        print("Impossible!")
    else:
        print("No luck in that number, thats not my password...")
        exit()
print(f"Wow, your numbers really must be lucky: {flag}")
