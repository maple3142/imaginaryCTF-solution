from lupa import LuaRuntime
import requests
import string


def get_check_index(code, mx):
    if "bxor" in code:
        # lupa installed using pip doesn't support lua 5.3
        return [20 ^ 30]
    lua = LuaRuntime(unpack_returned_tuples=True)
    lua.execute(code)
    check = lua.eval("check")
    return [i for i in range(mx) if check(i)]


url = "https://cookie-jar.ictf.iciaran.com/"
chs = "{_}" + string.digits + string.ascii_letters
mx = 100
flag = bytearray(mx)
for c in chs:
    code = requests.get(url, cookies={"char": c}).text
    print(c)
    print(code)
    for i in get_check_index(code, mx):
        flag[i] = ord(c)
    print(flag)
    print()

# ictf{r3ver51n9_w17h0u7_full_s0urc3}
