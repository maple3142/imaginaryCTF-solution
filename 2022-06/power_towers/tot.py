from sympy import totient
from Crypto.Util.number import bytes_to_long,getPrime
import random
def powertower(l,mod):
    if l==[]:
        return 1
    an=1
    tot=totient(mod)
    for i in range(len(l)-1,-1,-1):
        if an>1000:
            return pow(l[0],powertower(l[1:],tot)+tot,mod)
        an=l[i]**an
    return an%mod
p=getPrime(64)
while p%15!=2:
    p=getPrime(64)
flag='0'+bin(bytes_to_long(open('flag.txt','rb').read()))[2:]
print('The prime is:',p)
print('The length of the flag is:',len(flag))
while True:
    print('Your seed is:')
    seed=int(input())
    random.seed(seed)
    newFlag=list(flag)
    random.shuffle(newFlag)
    ptinput=[int(x)*2+3 for x in newFlag]
    print('The hash of the flag shuffled with your seed is',powertower(ptinput,p))