#!/usr/bin/env python3.9


mem = [0]*2**16
free_space = [(0, 2**16 - 1)]
sizes = {}

def coalesce():
    global free_space
    free_space = sorted(free_space, key=lambda x:x[0])
    for i in range(len(free_space)-1, 0, -1):
        if free_space[i][0] == free_space[i-1][1]:
            free_space[i-1] = free_space[i-1][0], free_space[i][1]
            free_space.pop(i)

def remove_empty():
    global free_space
    for i in range(len(free_space)-1, -1, -1):
        if free_space[i][0] >= free_space[i][1]:
            free_space.pop(i)

def malloc(n):
    if n <= 0:
        return 0
    for i, pair in reversed(list(enumerate(free_space))):
        start, end = pair
        if end-start > n:
            sizes[end-n] = n
            free_space[i] = (start, end-n)
            coalesce()
            remove_empty()
            return end-n
    print("Out of space!")
    print("You're probably doing something horribly wrong.")
    return 0

def free(ptr):
    global free_space, sizes
    free_space.append((ptr, ptr+sizes[ptr]))
    del sizes[ptr]
    coalesce()
    remove_empty()

def realloc(ptr, size):
    global free_space, sizes
    cur_size = sizes[ptr]
    if size <= cur_size:
        return
    size_diff = size - cur_size
    for i, pair in enumerate(free_space):
        if pair[0] == ptr + cur_size and pair[1] >= ptr + size:
            sizes[ptr] = size
            free_space[i] = pair[0]+size_diff, pair[1]
            coalesce()
            remove_empty()
            return ptr
    newptr = malloc(size)
    write(newptr, read(ptr))
    free(ptr)
    return newptr

def print_heap():
    sorted_sizes = sorted([(i,sizes[i]) for i in sizes], key=lambda x:x[0])
    print()
    print("="*80)
    for ptr, sz in sorted_sizes:
        print(f"{ '{:5d}'.format(sz)} bytes mapped from {hex(ptr)} - {hex(ptr+sz)}")
    print("="*80)
    print()

def write(ptr, data):
    if ptr == 0:
        return 0
    for i, c in enumerate(data):
        mem[ptr+i] = c

def read(ptr):
    return bytes(i%256 for i in mem[ptr:ptr+sizes[ptr]])

def buffered_write(ptr, size, data):
    for i, c in enumerate(data):
        if i > size and size < 8192: # mimicking result of integer overflow here
            size *= 2
            ptr = realloc(ptr, size)
        if i > 16384:
            print("Exceeded int range!")
            print("Segfaulting...")
            exit()
        mem[ptr+i] = c
    return ptr, size

def strlen(inp):
    for i, c in enumerate(inp):
        if c == 0:
            return i
    return len(inp)

def strdup(inp):
    size = strlen(inp)
    ptr = malloc(size)
    write(ptr, inp[:size])
    return ptr

def main():
    password = malloc(16)
    write(password, b"0123456789abcdef") 
    pattern_size = int(input("Enter initial chunk size: "))
    assert(pattern_size >= 16)
    patterns = malloc(pattern_size)
    inp = "aaaa"
    dynstr = malloc(1)
    dynstr_size = 1
    while len(inp) > 0:
        inp = input("Enter filename: ")
        inp = bytes(ord(i) for i in inp)
        dynstr, dynstr_size = buffered_write(dynstr, dynstr_size, inp)
        # print_heap() # for debugging, because gdb isn't a thing
        newname = strdup(inp)
        if len(inp) > 1 and inp[1] == 98: # recording only the patterns that have 'b' as the second letter
            patterns = realloc(patterns, pattern_size+1)
            pattern_size += 1
            mem[patterns+pattern_size-1] = newname
    if read(password) == b"heapfengshuigod!":
        print(open("flag.txt").read())
    print(read(password))

if __name__ == '__main__':
    main()