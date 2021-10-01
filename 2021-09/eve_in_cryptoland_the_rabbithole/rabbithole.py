#!/usr/bin/env python3

from secrets import randbelow
from redacted import r, key, flag
# r is supposed to be random but I computed it randomly beforehand to limit server load :D

p = 95448141706840057074981648919653158061602940212059310641262844843045070085413
g = 2
y = pow(g, key, p)

def prove_ownership():
    print("'Is your proof so flawless as to resist my ways?', you laugh. 'I shall prove to you I am the one true owner of the key!'")
    t = int(input('t = '))
    c = randbelow(p)
    print("The door clearly isn't convinced by your words, but challenges you nonetheless.")
    print(f'{c = }')
    print("'I bet you can't even beat this. What is your answer?'")
    s = int(input('s = '))
    return pow(g, s, p) == t * pow(y, c, p) % p

def demand_proof():
    print("Snorting, you say with disdain 'Ha! You must think you are so smart, door. But do you even know your own key?'",
          "The handle wiggles in indignation and the door snarls:",
          "'That's some sharp tongue you got there, lass. Let me show you the extent of my knowledge, and we will see if you act so high and mighty after that.'")
    print("'Here is my randomness:'")
    t = pow(g, r, p)
    print(f'{t = }')
    print("'Issue your challenge!', adds the door. Confidence permeates its words.")
    c = int(input('c = '))
    s = (r + c*key) % (p - 1)
    print("Somehow the door manages to look smug. 'My proof is flawless, feel free to test it~.'")
    print(f'{s = }')

print("You find yourself in a great hall, so high that the ceiling fades away in shadows. Surrounding you are many doors of varying shapes, size, and texture.", 
      "One particularly catches your attention, for light shines from below the handle; surely this must be the exit. Unfortunately, no key lie in sight.",
      "'Who even needs keys!', you think to yourself. 'Unlike that loser Alice, I am quite adept at forging them.'")

print("Looking through the keyhole, you see a lovely little garden. At one edge stands a flag, some message inscribed ─ you are too far, however, to read it.",
      "Suddenly, the door creaks and a voice reach your ears. 'I only open for the owner of the key! Prove me it belongs to you, only then may you pass through.',",
      " it claims.")

demand_proof()

if prove_ownership():
    print("The handle drops agape. 'H-How? This is impossible! You shouldn't know the key!'")
    print("'...'")
    print("'I can't believe I have to let you pass...'")
    print("The door opens as slowly as it can, grumbling all the while about some irksome brat.",
          "Right after you pass through the opening, it slams so hard a piece of wall falls on your head.",
         f"Its snickers acommpagny you as you move on to the garden; there you can see the flag. Some hooligans wrote '{flag}' on it.")
    print("You continue down the paths, wondering how to get out of this strange place where walls listen and doors talk.")
else:
    print("'Hohoho, where is your cheekiness gone now, huh? You can remain in this hall forever for all I care!'")
