# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.10 | packaged by conda-forge | (default, May 11 2021, 07:01:05) 
# [GCC 9.3.0]
# Embedded file name: signature_meme.py
# Compiled at: 2021-02-11 06:24:21
# Size of source mod 2**32: 2648 bytes
import random, string, hashlib, base64, time, platform, fastecdsa.curve, fastecdsa.point
CHALLENGE_LENGTH = 20
CURVE = fastecdsa.curve.secp256k1
PRIVKEY = None
PUBKEY = None

def read_key():
    global PRIVKEY
    global PUBKEY
    random.seed('%s.%d.%s.%s' % (platform.platform(), time.time(), platform.uname(), platform.node()))
    with open('key') as (f):
        p, x, y = map(int, map(str.strip, f.readlines()))
    PRIVKEY = p
    PUBKEY = fastecdsa.point.Point(x, y, curve=CURVE)


def encode(x):
    h = hex(x)[2:]
    if len(h) & 1:
        h = '0' + h
    return base64.b64encode(bytes.fromhex(h)).decode('utf-8')


def decode(x):
    return int(bytes.hex(base64.b64decode(x.encode('utf-8'))), 16)


def sign(msg):
    k = random.randrange(CURVE.q)
    t = CURVE.G * k
    c = int(hashlib.sha512(str(t).encode() + msg.encode('utf-8')).hexdigest(), 16)
    s = k + PRIVKEY * c
    return '{}.{}.{}'.format(encode(t.x), encode(t.y), encode(s))


def validate_signature(msg, s):
    try:
        s = s.split('.')
        if len(s) != 3:
            return False
        x, y, s = map(decode, s)
    except:
        return False
    else:
        t = fastecdsa.point.Point(x, y, curve=CURVE)
        c = int(hashlib.sha512(str(t).encode() + msg.encode('utf-8')).hexdigest(), 16)
        return CURVE.G * s == t + PUBKEY * c


def generate_challenge():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(CHALLENGE_LENGTH))


def main():
    read_key()
    print('Welcome to the management server, as a reference, here is our public key:')
    print(PUBKEY)
    print()
    while True:
        try:
            m = input('What do you want to do?\n1. Sign a message\n2. Get a flag\n3. Quit\n> ')
        except:
            print('Goodbye!')
            break

        if m.strip() == '1':
            m = input('What message would you like to sign?\n> ')
            if m.strip() == 'Hello, world!':
                print('Thank you, here is your signature:')
                print(sign(m))
            else:
                print("I'm sorry, I can't endorse that statement")
        else:
            if m.strip() == '2':
                r = generate_challenge()
                print('Please sign the following message to get access (without quotes): %r' % r)
                s = input('> ')
                if validate_signature(r, s):
                    print(open('flag.txt').read())
                    break
                else:
                    print('WRONG!')
            else:
                if m.strip() == '3':
                    print('Goodbye')
                    break
                else:
                    print('What are you saying, exactly?')


if __name__ == '__main__':
    main()
# okay decompiling signature_meme.pyc
