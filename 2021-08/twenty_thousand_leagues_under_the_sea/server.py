#!/usr/bin/env python3

from re import compile, match, error
from secrets import randbelow
from time import sleep

def validate_regex(r):
    if any(char in r for char in ['.', '*', '+']):
        print("That character is blacklisted!")
        return False
    try:
        if r.isprintable():
            compile(r)
            return True
    except error as e:
        pass
    print(f"That is NOT a Regular Expression. No one said pwn.")
    return False

with open("TwentyThousandWordlist.txt") as word_list:
    words = word_list.read().split()

magic_word = words[randbelow(len(words))]

print('''
                             `<vr^:-                                  
                           `WQc:-.,iP}-                               
            `..-':-       V0r       `(o<                              
          .-       *     *Q!:         =}_                             
         `  ~6GL!~=._    yr--~.     .y`}<                             
         rru_ .:.   '=`  Kl ,!v ~.,__`*5:                             
         Q- }(rrWBQL  :x~By=_:*::_}__==<                              
        v .=Q`   `G0W` :oy~^` :~}`!-'xk       `    `` -               
       ^ `) }x  ` `=lkWx_ :iOy~! *igoyi^_:,-'~?kWwuV*  *              
_i(`.!*`   .`Z:          `,~*,.  _z>*T`   ``::,~`   zT`y'             
  '         yx  _\\TVzG5ml^`    IW`    -!.   -,xiux<  ':>_             
            ,=.'<:'-:~v}x`  ^Gg@BL(.`  'vB8sV, :wk3OPT!,,:~*rrLx^<*,' 
          \\~yRe.r}-:__=:- -*\\V~`=T3ZzV_  =<,~)e `  <~m^,!=::,`    -_u<
          3V\\v_.  ~,  !`_xx~  ```  :*mw   .   `~`-~ ~`           .cvv 
       `:v- `    `  rv*  <Q.-,:  .-::    _    * ** .                  
    ':-             `<o,  K!'``:,.          __` u _                   
    -,:                 '  vXx:-!*. ``    -*x:   *L}cv                
                          ``.vzx*vvr_`^_ <mx       .xQ                
                                <:~ _**  Q=  '~   ^x.                 
                                         `<!~,`                       

            Welcome to Twenty Thousand Leagues Under the Sea! 

Okay... you got me. 
    It is Regular Expressions, not Leagues... 
    And only twenty, not twenty thousand...

You may make ask twenty questions in regular expression form in order
to guess the word I have chosen from 20,000 Leagues Under The Sea.

If your guess is exactly the word I am thinking, I will surrender
and wave the proverbial flag.

Ready?

''')
# sleep(1)
for x in range(1,21):
    print(f"RegEx Number {x}, or exact guess: " if x < 20 else "Final guess! What is the word?")
    user_regex = input()
    if magic_word == user_regex:
        print(f"Correct!")
        with open("flag.txt") as flag:
            print(flag.read().strip())
        break
    if validate_regex(user_regex):
        if match(user_regex, magic_word):
            print("Yes!")
        else:
            print("No!")
    if x >= 20:
        print(f"You lose! The word was: {magic_word}\\n\\nWhen you try again, I will pick a different word.")
        break


