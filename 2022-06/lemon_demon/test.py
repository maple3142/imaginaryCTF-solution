import numpy as np
from numpy.fft import fftfreq, fft, ifft, rfft, irfft
from scipy.io import wavfile



fs, data = wavfile.read("flag-new.wav")

# chunk = []
# chunks = []
# zerocnt = 0
# for t, x in enumerate(data):
#     if x == 0:
#         zerocnt += 1
#         if zerocnt >= 2500:
#             if len(chunk) > 500:
#                 print(t/fs,x)
#                 chunks.append(chunk)
#                 chunk = []
#                 zerocnt = 0
#     else:
#         chunk.append(x)

# freqs = fftfreq(512, d=1 / fs)
# cur = fft(chunks[3])
# for x in chunks[:5]:
#     print(x)
# for f, a in zip(freqs, cur):
#     print(f, np.abs(a))
# print(len(chunks))

fd = fft(data)
freqs = fftfreq(2048, d=1/fs)
# for f, (i, d) in zip(freqs, enumerate(fd)):
#     if f <= 20000:
#         # print('set', f, i)
#         fd[i] = 0
#     else:
#         print('good', f, d)
data2 = np.real(ifft(fd))
wavfile.write(f"flag-new2.wav", fs, data2)

# for t, x in enumerate(data):
#     if x!=0 and abs(x)<=200000:
#         print(t/fs,x)
