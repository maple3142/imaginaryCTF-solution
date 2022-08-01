#!/usr/bin/env python3

from sqlite3 import *
from hashlib import sha256
from os import system
from base64 import b64encode

def pad(b, l):
    c = (l-(len(b)%l))
    return b + bytes([c]*c)

system('rm -f ../users.db')
conn = connect("../users.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL ,
    password TEXT NOT NULL
);
''')

password = b'password'

for i in range(65536):
    salt = b64encode(pad(bytes.fromhex('{:04x}'.format(i)), 16))
    hsh = sha256(salt+password).hexdigest()
    cur.execute("insert into users values (?, ?)", ('admin', hsh))
    print(i)
conn.commit()
system('tar -cvPf ../../compressed.tar ../users.db')
system('base64 ../../compressed.tar | tr -d "\\n" > ../../b64')
