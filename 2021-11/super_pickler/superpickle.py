#!/usr/bin/env python3.9

import pickle
import marshal
import re

from tree import flag

def super_pickle(obj):
    ret = {attr:marshal.dumps(getattr(obj, attr).__code__) for attr in dir(obj)
                if hasattr(getattr(obj, attr), "__code__")}
    ret["__"] = pickle.dumps(obj)
    return pickle.dumps(ret)

f = open("pick", "wb")
b = ''.join(chr(i) for i in super_pickle(flag))
b = re.sub("/mnt.*/", "[REDACTEDREDACTEDREDACTEDREDACTEDREDACTEDREDACT]/", b) # to avoid doxxing myself
b = bytes(ord(i) for i in b)
f.write(b)
