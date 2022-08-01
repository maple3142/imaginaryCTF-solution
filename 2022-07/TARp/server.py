#!/usr/bin/env python3

from os import urandom
from base64 import b64encode, b64decode
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from sqlite3 import *
import tarfile

from requests import get

current_user = None
salt = None

def extract():
    url = input("Please enter the URL of your tarfile: ")
    f = BytesIO(get(url).content)
    tarfile.TarFile(fileobj=f).extractall('./extracted')
    print("Extracted successfully.")

def view():
    files = Path('./extracted').rglob('*')
    print("Which file would you like to view?")
    enum = list(enumerate(files))
    for i, file in enum:
        print(f'{i+1}) {file.name}')
    print()
    inp = int(input('>>> '))
    print('='*80)
    print(enum[inp-1][1].open().read())
    print('='*80)

def add_user(username, password):
    global salt
    hsh = sha256(salt+password)
    conn, cur = get_sql()
    cur.execute("insert into users values (?, ?)", (username, hsh.hexdigest()))
    conn.commit()
    cur.close()
    conn.close()

def make_acc():
    username = input('Enter new username: ')
    if username == 'admin':
        print("Can't redefine admin!")
        return
    password = input('Enter new password: ')
    add_user(username, password.encode())

def handle_log_io():
    global current_user, salt
    if current_user is not None:
        current_user = None
        return
    username = input("Username: ")
    password = input("Password: ").encode()
    conn, cur = get_sql()
    cur.execute('select username from users where username = ? and password = ?',
        (username, sha256(salt+password).hexdigest()))
    if row := cur.fetchone():
        current_user = row[0]
        print(f'Logged in as {current_user}')
    else:
        print("Could not authenticate credentials. Please try again.")
    cur.close()
    conn.close()

def pad(b, l):
    c = (l-(len(b)%l))
    return b + bytes([c]*c)

def flag():
    global current_user
    if current_user == 'admin':
        print(open('flag.txt').read())
        exit(0)
    else:
        print(f"Sorry, user '{current_user}' doesn't have access to the flag.")

def get_sql():
    conn = connect("users.db")
    cur = conn.cursor()
    return conn, cur

def setup():
    global salt, conn, cur
    salt = b64encode(pad(urandom(2), 16))
    conn, cur = get_sql()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT UNIQUE ON CONFLICT REPLACE NOT NULL ,
        password TEXT NOT NULL
    );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    add_user('admin', b64encode(urandom(32)))

def menu():
    global current_user
    print("Welcome to TARp!")
    print("1) Extract tar file")
    print("2) View extracted files")
    print("3) View source")
    print("4) Make new account")
    if current_user is None:
        print("5) Login")
    else:
        print('5) Logout')
    print("6) View flag")
    print()
    inp = input(">>> ")
    if '1' in inp: 
        extract()
    elif '2' in inp:
        view()
    elif '3' in inp:
        print('='*80)
        print(open(__file__).read())
        print('='*80)
    elif '4' in inp:
        make_acc()
    elif '5' in inp:
        handle_log_io()
    elif '6' in inp:
        flag()
    else:
        print('Unrecognized input!')
    print()

if __name__ == '__main__':
    setup()
    while 1:
        menu()
