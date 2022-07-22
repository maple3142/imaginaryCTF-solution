import gmpy2
from tqdm import tqdm
import random

n = gmpy2.mpz(
    63038895359658613740840475285214364620931775593017844102959979092033246293689886425959090682918827974981982265129797739561818809641574878138225207990868931316825055004052189441093747106855659893695637218915533940578672431813317992655224496134300271524374912502175195904393797412770270676558054466831561609036199966477
)
e = 65537
ct = 60515029337308681079476677877525631415600527185785323978384495461916047877351538207473264679842349366162035496831534576192102896080638477601954951097077261305183669746007206897469286005836283690807247174941785091487066018014838515240575628587875110061769222088950451112650700101446260617299040589650363814995825303369

ar = list(range(2, 2**25))
random.shuffle(ar)
a = gmpy2.mpz(2)
for p in tqdm(ar):
    a = gmpy2.powmod(a, p, n)
    g = gmpy2.gcd(a - 1, n)
    if 1 < g < n:
        print(g)
        break
# 434654113480567754843550047971815161129803871913933783262402156469121832491983228916050415001822989063035108089351335052513369073826096294477221516463704292443