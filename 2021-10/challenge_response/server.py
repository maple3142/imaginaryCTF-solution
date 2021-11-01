#!/usr/bin/env python3.9

from database import logins, flag, secret_hash, challenge
from dis import dis

currentUser = None

def login():
    global currentUser
    print("Enter username: ")
    user = input()
    if user not in logins:
        print("That user does not exist!")
        return
    if challenge(user, logins):
        print("Login success!")
        currentUser = user
    else:
        print("Invalid password.")

def logout():
    print("Logging out...")
    currentUser = None

def get_flag():
    if currentUser == 'admin':
        print(flag)
        exit()
    else:
        print("Insufficient permissions.")
        print()
        print("This incident has been reported.")

def create_user():
    print("NOTE: this channel is NOT encrypted!")
    print("ALL communications are subject to being snooped by a man-in-the-middle attack.")
    print("Please make sure no one is listening to your traffic before you enter your password in cleartext.")
    print()
    print("Please enter your username: ")
    user = input()
    if user in logins:
        print("That user already exists!")
        return
    print("Note that for safety, we do not store passwords in plaintext.")
    print("Instead, they are stored using our custom hashing algorithm.")
    print()
    print("Please enter your password: ")
    logins[user] = secret_hash(input())

def hack_server():
    print("Oh golly gosh - it seems that you hacked the server with your binary input!")
    print("I guess I have to give you the server database now...")
    print()
    print("You won't be able to use it, though - all the passwords are hashed!")
    print()
    [print(f'{i}: {logins[i]}') for i in logins]
    print()
    dis(secret_hash)
    print()
    print("Press enter to continue.")
    input()

def menu():
    print('='*80)
    print("Super Secure Server v0.12")
    print('='*80)
    if currentUser == None:
        print("1. Login")
    else:
        print(f"Current user: {currentUser}")
        print()
        print("1. Switch User")
    print("2. Create Account")
    print("3. Get Flag")
    if currentUser is not None:
        print("4. Logout")
    inp = input('>>> ')
    if '1' in inp:
        login()
    elif '2' in inp:
        create_user()
    elif '3' in inp:
        get_flag()
    elif '4' in inp:
        logout()
    elif '\x7f' in inp:
        hack_server()

def main():
    while True:
        menu()
        print()

if __name__ == '__main__':
    main()