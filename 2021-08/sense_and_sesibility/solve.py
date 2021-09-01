
filter = ".txt"
def gcd(prime, real):
    return [root for root in real if sorted(root) == sorted(prime)]
def isSTriangle(area):
    return str(area)

total = sum (1 for f in filter)
negative = '-'
remainder = total // total
imaginary = total + remainder
Euler_constant = negative + isSTriangle(total >> imaginary)
Euler_area = (total << remainder + remainder) * (imaginary + total + remainder) + remainder

with open(isSTriangle(Euler_area) + Euler_constant + filter) as SaS:
    while isSTriangle(Euler_area + total * imaginary) + isSTriangle(remainder) not in SaS.readline():
        pass
    real_part = []
    for imaginary_part in SaS.read().splitlines():
        real_part.extend(imaginary_part.split())
    summation = sorted(set([greekLetter for greekLetter in real_part if greekLetter.isalpha() and len(greekLetter) == total]))

    flag_real_part = [Xvar for Xvar in summation if len(gcd(Xvar, summation)) > (total>>remainder)]
    print(f"ictf{{{'_'.join(flag_real_part[::(total>>remainder)])}}}")
