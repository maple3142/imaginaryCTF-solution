n = 76949695802461994677509945383479695643067481842087701926881504886493732761795336091839430933758023107107858611906678976191776750317260066941217882367556248442929218329001406172137508707009376434379416341044772163984829685269163874311355712440565221383625726060639267047472007036556083729475447761221888000000


def partial_factor(n):
    # based on ecm.factor
    B1 = [1 << i for i in range(1, 12)]
    fs = []
    ns = [n]
    try:
        while ns:
            n = ns.pop(0)
            if n.is_prime():
                fs += [n]
                continue
            if n.nbits() < 15:
                for p, e in n.factor(algorithm="pari"):
                    fs += [p] * e
                continue
            if n.is_perfect_power():
                p, e = n.perfect_power()
                fs += [p] * e
                continue
            fac = [n]
            i = 0
            while len(fac) == 1 and i < len(B1):
                fac = ecm.find_factor(n, B1=B1[i])
                i += 1
            ns += fac
        fs.sort()
        return fs
    except KeyboardInterrupt:
        # press Ctrl-c when you want to stop
        return sorted(fs + [n])


partial_factor(n)
