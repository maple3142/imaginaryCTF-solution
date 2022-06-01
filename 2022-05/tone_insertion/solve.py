import numpy as np
from numpy.fft import fftfreq, rfft, irfft
from scipy.io import wavfile


def power(signal):
    return np.mean(np.float64(signal) ** 2)


fs, data = wavfile.read("tone.wav")
seq = data.T[0] >> 15
seq2 = data.T[1] >> 15
target_idx = (fftfreq(512, d=1 / fs)).tolist().index(21963.8671875)


def extract(s, i, j):
    xs = rfft(s)
    xs[:i] = 0
    xs[j + 1 :] = 0
    return irfft(xs)


bits = ""
for i in range(0, len(seq[: 64 * 8 * 512]), 512):
    if i + 512 >= len(seq):
        break
    y1 = extract(seq[i : i + 512], target_idx, target_idx)
    v1 = power(y1)
    y2 = extract(seq2[i : i + 512], target_idx, target_idx)
    v2 = power(y2)
    print(i // 512, v1, v2)
    if v1 > v2 and v1 > 10000:
        bits += "1"
    else:
        bits += "0"
print((int(bits, 2)).to_bytes(len(bits) // 8, "big"))
