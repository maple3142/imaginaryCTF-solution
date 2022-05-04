from secrets import randbelow
from redacted import flag

p = 115792089237316195423570985008687907853269984665640564039457584007913129870127
g = 5
x = randbelow(p)
y = pow(g, x, p)

def nonces():
    a = randbelow(p)
    b = randbelow(p)
    r = randbelow(p)
    while 1:
        yield r
        r = (a*r + b) % (p - 1)

def test_truth():
    print("A scarecrow guards the roads. You come to it, asking for the right to walk on your chosen path.")
    t = int(input('t = '))
    c = randbelow(p)
    print("The scarecrow issues a challenge to test your understanding of the truth.")
    print(f'{c = }')
    print("It waits unmoving for your answer.")
    s = int(input('s = '))
    return pow(g, s, p) == t * pow(y, c, p) % p

def proof(r):
    print("'I claim to detain the truth. What is your challenge?'")
    c = int(input('c = ')) % (p - 1)
    if not c:
        exit()

    t = pow(g, r, p)
    s = (r + c*x) % (p - 1)
    print("'I shall present you my proof.'")
    print(f'{t = }')
    print(f'{s = }')

print("As you wander down the path, your gaze fall upon many wonders. A bush that grows pears, a tree adorned with flowers a myriad colors; "
      "all of these and stranger plants lay commonsight beside the path. 'What a strange land I came to', you mutter. "
      "Deep in your thoughts, you don't notice the blue wisps that grow thicker and thicker as you go on, until you come face to face with a huge caterpillar "
      "that hangs off a tree in a small clearing. It ─ or is it he? ─ sports a pipe, from which comes the haze.",
      "'Who are you?', you ask.",
      "'Me? Just one oracle, that cannot foretell.', it shrugs.",
      "It takes a deep breath, filling the clearing with smoke.",
      "'I can, however, see that you are one lost soul. There are a great many ways, "
      "but only one would lead you to the end of our world, and, ah, the beginning of yours.'",
      "It ponders; the smog of his pipe takes various geometrical shapes and circles around you.",
      "'I shall grant you four dreams; may them reveal an inkling of your destination.'",
      "As it finishes its speech, the wind hurls the fog toward you. You only see the caterpillar releasing a continuous stream of mist "
      "before your vision fades in blue. Words echo within the cloud: 'There is no truth without proof, and there is no proof without challenge.'",
      "", sep='\n')

r = nonces()
print("A shadowy figure rises; it is that of an old monk, who quietly lectures you.")
proof(next(r))
print("The world shivers, and you are a knight fighting for your honor. You challenged him because he had spread lies.")
proof(next(r))
print("The arena becomes a conference room, and you sit on a chair. You listen intently to Bruce Schneier's speech.")
proof(next(r))
print("The chair lies behind a desk, and you interrogate the suspect. She tells you her version of the story.")
proof(next(r))
print("You are standing at a crossroads. No path is the right one, but one of them is wrong.")

wrong_choice = not test_truth()
print("The blue landscape slowly dissipates, leaving you in the middle of a road. The caterpillar or the clearing are nowhere to be seen. "
      "You move onward.")

if wrong_choice:
    print("After a while, the road ends without warning. You are at the edge of a dark forest, not knowing from whence you came or where to go. "
          "Once again, you are lost.")
else:
    print("The road is long and you rest on a rock. Something has been engraved here by the same hooligans as before. "
         f"Squinting your eyes, you manage to read '{flag}'")
