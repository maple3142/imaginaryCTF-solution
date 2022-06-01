import numpy as np
from numpy.fft import fft, ifft, fftfreq, rfft, irfft
from scipy.fftpack import dct, idct
from scipy.io import wavfile
from matplotlib import pyplot as plt



def generate_tone(freq, length, fs):
    x = np.arange(length) / fs
    return np.sin(2*np.pi*freq*x)

def power(signal):
    return np.mean(np.float64(signal)**2)

def sign(x):
    return x/np.abs(x) if x != 0 else 0

def encode_tone(data, msg, fs=44100):
    # msg is bytes
    msg_bits = ''.join('{:08b}'.format(i) for i in msg)
    print(msg_bits)

    idx = 0
    frame_size = 512

    ratios = []
    data = np.int32(data)
    
    while len(msg_bits) > 0:
        if 512*(idx+1) > len(data):
            break
        bit = msg_bits[0]
        msg_bits = msg_bits[1:]
        if bit == '0':
            idx += 1
            continue
        tone = generate_tone(21963.8671875, 512, fs)*1e3
        for j in range(512):
            data[512*idx+j][0] += tone[j]

        idx += 1

        if idx%1000 == 0:
            print(idx)
    return data*2**15


fs, orig = wavfile.read("sample.wav")
orig = np.int32(orig)
data = encode_tone(orig.copy(), b'ictf{test_flag}', fs)
seq = (data.T[0]>>15)&0x3ff
seq2 = (data.T[1]>>15)&0x3ff
seq = (orig.T[0])&0x3ff
seq2 = (orig.T[1])&0x3ff
target_idx = (fftfreq(512)*fs).tolist().index(21963.8671875)
# print(fftfreq(512)*fs)
def extract(s,i):
    xs = fft(s)
    xs[:i] = 0
    xs[i+1:]=0
    return ifft(xs)

bits = ''
for i in range(0,len(seq[:2*8*512]), 512):
    if i+512>=len(seq):
        break
    y1 = extract(seq[i:i+512], target_idx)
    v1 = power(np.abs(y1))
    
    y2 = extract(seq[i:i+512], target_idx - 1)
    v2 = power(np.abs(y2))
    # y2 = extract(seq2[i:i+512])
    # v2 = power(np.real(y2))
    # v1 = np.abs(rfft(seq[i:i+512])[target_idx])
    # v2 = np.abs(rfft(seq2[i:i+512])[target_idx])
    print(i//512, v1, v2)
    if v1 > v2:
        bits += '1'
    else:
        bits += '0'

#     plt.plot(np.abs(np.real(y)), label=f'#{i//512}r')
#     plt.plot(np.abs(np.imag(y)), label=f'#{i//512}i')
# plt.legend()
# plt.show()
    # print(np.abs(y).mean(),np.real(y).mean(),np.imag(y).mean())
print((int(bits,2)).to_bytes(len(bits)//8,'big'))
print(fs)
