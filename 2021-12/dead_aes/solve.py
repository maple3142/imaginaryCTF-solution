from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import *
from random import Random
from tqdm import tqdm

# io = process(["python", "deadaes.py"])
io = remote("spclr.ch", 1360)


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


def get_rand():
    io.sendlineafter(b"option: ", b"E")
    io.sendlineafter(b"message: ", b"peko")
    io.recvuntil(b"is ")
    ct = bytes.fromhex(io.recvlineS().strip()[:-1])
    io.recvuntil(b"is ")
    key = bytes.fromhex(io.recvlineS().strip()[:-1])
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(ct)
    iv = xor(dec, pad(b"peko", 16))

    key = bytes_to_long(key)
    iv = bytes_to_long(iv)
    return [
        (key >> 96) & 0xFFFFFFFF,
        (key >> 64) & 0xFFFFFFFF,
        (key >> 32) & 0xFFFFFFFF,
        key & 0xFFFFFFFF,
        (iv >> 96) & 0xFFFFFFFF,
        (iv >> 64) & 0xFFFFFFFF,
        (iv >> 32) & 0xFFFFFFFF,
        iv & 0xFFFFFFFF,
    ]


class MT19937Recover:
    """Reverses the Mersenne Twister based on 624 observed outputs.
    The internal state of a Mersenne Twister can be recovered by observing
    624 generated outputs of it. However, if those are not directly
    observed following a twist, another output is required to restore the
    internal index.
    See also https://en.wikipedia.org/wiki/Mersenne_Twister#Pseudocode .
    """

    def unshiftRight(self, x, shift):
        res = x
        for i in range(32):
            res = x ^ res >> shift
        return res

    def unshiftLeft(self, x, shift, mask):
        res = x
        for i in range(32):
            res = x ^ (res << shift & mask)
        return res

    def untemper(self, v):
        """Reverses the tempering which is applied to outputs of MT19937"""

        v = self.unshiftRight(v, 18)
        v = self.unshiftLeft(v, 15, 0xEFC60000)
        v = self.unshiftLeft(v, 7, 0x9D2C5680)
        v = self.unshiftRight(v, 11)
        return v

    def go(self, outputs, forward=True):
        """Reverses the Mersenne Twister based on 624 observed values.
        Args:
            outputs (List[int]): list of >= 624 observed outputs from the PRNG.
                However, >= 625 outputs are required to correctly recover
                the internal index.
            forward (bool): Forward internal state until all observed outputs
                are generated.
        Returns:
            Returns a random.Random() object.
        """

        result_state = None

        assert len(outputs) >= 624  # need at least 624 values

        ivals = []
        for i in range(624):
            ivals.append(self.untemper(outputs[i]))

        if len(outputs) >= 625:
            # We have additional outputs and can correctly
            # recover the internal index by bruteforce
            challenge = outputs[624]
            for i in range(1, 626):
                state = (3, tuple(ivals + [i]), None)
                r = Random()
                r.setstate(state)

                if challenge == r.getrandbits(32):
                    result_state = state
                    break
        else:
            # With only 624 outputs we assume they were the first observed 624
            # outputs after a twist -->  we set the internal index to 624.
            result_state = (3, tuple(ivals + [624]), None)

        rand = Random()
        rand.setstate(result_state)

        if forward:
            for i in range(624, len(outputs)):
                assert rand.getrandbits(32) == outputs[i]

        return rand


mt = MT19937Recover()
rnd = mt.go(sum([get_rand() for _ in tqdm(range(624 // 8))], []))


def gen(rnd):
    # weird order of operations or whatever
    # but make sure to separate the x<<n from other stuff with parentheses
    a = rnd.getrandbits(32)
    b = rnd.getrandbits(32)
    c = rnd.getrandbits(32)
    d = rnd.getrandbits(32)
    return (a << 96) + (b << 64) + (c << 32) + (d)


key = long_to_bytes(gen(rnd)).rjust(16, b"\x00")
iv = long_to_bytes(gen(rnd)).rjust(16, b"\x00")

io.sendlineafter(b"option: ", b"R")
io.recvuntil(b"is ")
ct = bytes.fromhex(io.recvlineS().strip()[:-1])
flag = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), 16)
print(flag)

# ictf{find_iv_with_key_and_find_number_with_MT!}
