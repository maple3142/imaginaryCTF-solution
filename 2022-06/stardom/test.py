import numpy as np
from numpy.fft import fftfreq, rfft, irfft
from scipy.io import wavfile



fs, data = wavfile.read("alice.wav")

# print(data[:, 0][:80])
# ar = data[:, 1].tolist()[:1024]
# cur = ar[0]
# cnt = 1
# for i in range(1, len(ar)):
#     if ar[i]!=cur:
#         print(cur, cnt, i+1)
#         cur=ar[i]
#         cnt = 1
#     else:
#         cnt+=1

# fd = rfft(data)
# freqs = fftfreq(2048, d=1/fs)
# print(fd)
# print(freqs)
# print(fs)
# with open('alice.wav', 'rb') as f:
#     data = f.read()[0x2c:]
# import struct
# shorts = struct.unpack('H'*(len(data)//2), data)
    
# # Get all LSB's
# extractedLSB = ""
# for i in range(0, len(shorts)):
#         extractedLSB += str(shorts[i] & 1 )
# # divide strings into blocks of eight binary strings
# # convert them and join them back to string
# string_blocks = (extractedLSB[i:i+8] for i in range(0, len(extractedLSB), 8))
# decoded = ''.join(chr(int(char, 2)) for char in string_blocks)
# print(decoded[:500])
wavfile.write('out.wav', fs, data[:,:-1])
