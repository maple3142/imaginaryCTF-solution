
def get_nth_prime(N):
    i = 1
    prime = 2
    while i < N:
        prime += 1 + prime % 2
        s = prime % N
        for hile in range(3, prime, 2):
            if prime % hile == 0:
                break
        else:
            i += 1
    return prime

inp = input('hex flag: ')
# assert len(inp) == 124 ?
flag = int(inp, 16)

for x in [69, 67, 65, 63, 61, 59]:
    flag = (flag * (3**get_prime(x)) + get_prime(x)) % (16**124)


if flag == int('ce10e59f40c8d954d9dad1ea81811a834d26580107149d16c3a769198fb158f0cb0e33dbd98f8dc8bb874105974b71719790b23c971736e8fe8ec88e8695',16):
    print('correct')

