from PIL import Image
import numpy as np

primes = np.array([   2,    3,    5,    7,   11,   13,   17,   19,   23,   29,   31,
         37,   41,   43,   47,   53,   59,   61,   67,   71,   73,   79,
         83,   89,   97,  101,  103,  107,  109,  113,  127,  131,  137,
        139,  149,  151,  157,  163,  167,  173,  179,  181,  191,  193,
        197,  199,  211,  223,  227,  229,  233,  239,  241,  251,  257,
        263,  269,  271,  277,  281,  283,  293,  307,  311])

def xor(x,y):
    return bytes([a^b for a,b in zip(x,y)])
def tobits(b):
    return ''.join([f'{x:08b}' for x in b])
def tobytes(b):
    return bytes([int(b[i:i+8],2) for i in range(0,len(b),8)])

u1 = bytes.fromhex('88e703dc6d8f491880e415a65aba968b')
u2 = bytes.fromhex('5fd7f2db85ad4395a6b1975d21d5d7ba')
u3 = bytes.fromhex('c2f66e72caa74fbda813619de62a87e9')
img1 = Image.open('my_image.png')
img2 = Image.open('my_image_2.png')
img3 = Image.open('my_image_3.png')
ar1 = np.asarray(img1)
ar2 = np.asarray(img2)
ar3 = np.asarray(img3)
d12=ar1^ar2
d13=ar1^ar3
d23=ar2^ar3
d12[:64,primes,:].nonzero()

xx = ar2[:64,primes,:]
sx = ''
for i in range(64):
    sx+=str((xx[i,i,0])&1)+str((xx[i,i,2])&1)
