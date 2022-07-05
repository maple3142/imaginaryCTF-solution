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
# def tower2(l):
#     if len(l)==0:
#         return 1
#     return l[0]**tower2(l[1:])
# l = [1,0,0]
# l = [int(x)*2+3 for x in l]
# print(l)
# print(tower2(l)%p)
# print(powertower(l,p))

# powertower([int(x)*2+3 for x in flag],p)
# while True:
#     print('Your seed is:')
#     seed=int(input())
#     random.seed(seed)
#     newFlag=list(flag)
#     random.shuffle(newFlag)
#     ptinput=[int(x)*2+3 for x in newFlag]
#     print('The hash of the flag shuffled with your seed is',powertower(ptinput,p))
# from sage.all import GF

# F=GF(p)
# od5 = F(5).multiplicative_order()
# od3 = F(3).multiplicative_order()
# print(od5)
# print(od3)

print(powertower([5,3,5,3,5,3,3,3] + list(range(1,123)),p))
print(powertower([5,3,5,3,5,3,3,3] + list(range(124)),p))
