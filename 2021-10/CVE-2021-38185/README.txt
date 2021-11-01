This challenge is based off of my cpio CVE, CVE-2021-38185, details of which can be found here: https://lists.gnu.org/archive/html/bug-cpio/2021-08/msg00000.html.

I tried for so long to make this into an actual pwn challenge with C, but due to memory constraints, it just wasn't feasible. So, I've replicated the most interesting bits in Python.

A brief overview of the exploit: an integer overflow bug when parsing filenames to extract led to an out-of-bounds write on an mmap chunk. With lots of heap manipulation, you can overwrite the libc with a House of Muney attack, leading to arbitrary code execution.

Your goal is to reproduce the heap manipulation stuff. You can, of course, go looking through my exploit code, but I've not yet published a full writeup, and there's enough changes that the exact same code won't work. I've recreated the core memory functions from C here, and they *should* work exactly the same as mmap chunks. Note that 1 "byte" here is 1<<16 bytes in C, which is why this doesn't work as a hosted C challenge. 

Good luck, and I hope you enjoy!