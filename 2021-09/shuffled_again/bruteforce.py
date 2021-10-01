from subbreaker.breaker import Breaker
from concurrent.futures import ProcessPoolExecutor


with open(
    "/home/maple3142/workspace/SubstitutionBreaker/subbreaker/quadgram/EN.json"
) as f:
    breaker = Breaker(f)


def try_break(a, b):
    if b == 0:
        print(a)
    with open(f"unshuffled/{a}-{b}.txt") as f:
        txt = f.read()
    r = breaker.break_cipher(txt, max_rounds=5)
    if r.fitness > 85:
        print(a, b)
        print(r.fitness)
        print(r.plaintext)
        print(r.key)
        print(f"ictf{{{r.key+bytes([a,b]).hex()}}}")
        print()


with ProcessPoolExecutor(max_workers=8) as executor:
    fs = []
    for a in range(128, 256):
        for b in range(256):
            fs.append(executor.submit(try_break, a, b))
    for x in fs:
        x.result()

# ictf{hkuojarmcepzsyivbdngxqwtlfe866}
# similartothepreviousshufflingchallengeimagainincludingabunchofrandombabblingherejusttomakesuretheresenoughciphertexttodoanykindofmeaningfulstatisticalanalysisihopeyouhavefunwithitandilloutlinemyownsolvingstrategyherejusttohaveenoughfillerandthenineedtodolessextrawritingtohaveagoodwriteupforthechallengeafterthefactasbeforethekeyliesinbigramsyoucanbuildatheoreticalreferencefrequencyofbigramsandforeverypossiblepermutationkeymeasurehowclosethebigramfrequencyfortheresultingplaintextistothatreferenceonceyouhaveagoodunshuffledversionyoucanusesometoollikethequipqiupwebsitetoundothemonoalphabeticsubstitutionandrecoverthismessage
# run with quipquip:
# similar to the previous shuffling challenge im again including a bunch of random babbling here just to make sure theres enough ciphertext to do any kind of meaningful statistical analysis i hope you have fun with it and ill outline my own solving strategy here just to have enough filler and then i need to do less extra writing to have a good write up for the challenge after the fact as before the key lies in big rams you can build a theoretical reference frequency of bigrams and for every possible permutationkey measure how close the big ram frequency for the resulting plain text is to that reference once you have a good un shuffled version you can use some tool like the quipqi up website to undo the mono alphabetic substitution and recover this message
