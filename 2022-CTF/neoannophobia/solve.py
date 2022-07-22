from pwn import *

# context.log_level = "debug"

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
inv_months = {v: k for k, v in months.items()}


def recvdate(io):
    s = io.recvlineS().strip()
    mon, date = s.split(" ")
    mon = months[mon]
    date = int(date)
    return mon, date


def balance(mon, date):
    print(inv_months[mon], date)
    # https://en.wikipedia.org/wiki/Nim 2 heap
    p1 = 12 - mon
    p2 = 31 - date
    if p1 == p2:
        print("Already balanced :(")
        # already balance, choose any
        return inv_months[mon + 1], date
    m = min(p1, p2)
    p1 = m
    p2 = m
    mon = inv_months[12 - p1]
    date = 31 - p2
    print(mon, date)
    return mon, date


io = remote("neoannophobia.chal.imaginaryctf.org", 1337)
for rnd in range(100):
    print(rnd)
    io.recvuntil(b"----------\n")
    io.recvuntil(b"----------\n")
    while True:
        mon, date = balance(*recvdate(io))
        io.sendlineafter(b"> ", f"{mon} {date}".encode())
        if (mon, date) == ("December", 31):
            break
io.interactive()
# ictf{br0ken_game_smh_8b1f014a}
