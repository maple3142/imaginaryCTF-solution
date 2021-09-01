import gdb

gdb.execute(
    """
b unlink
commands
ret
c
end

b *(main+77)
commands
set *($rax) = 0
c
end

b *(main+224)
commands
set $eax = 1
c
end

b *(main+214)
commands
printf "%c\n", $al
end
"""
)

# ictf{jar_jar_is_just_an_elf_in_disguise_-_he_must_be_a_sith_lord_because_java_is_evil}
