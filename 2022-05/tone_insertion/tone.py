#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft

from hidden import hidden_msg

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


if __name__ == '__main__':
    fs, orig = wavfile.read("sample.wav")
    assert type(hidden_msg) is bytes
    new_data = encode_tone(orig, hidden_msg, fs=fs)
    wavfile.write(f"tone.wav", fs, new_data)
