import os

with open("flag.bf") as f:
    code = f.read()

with open("bf.c", "w") as f:

    def w(x):
        return f.write(x + "\n")

    w("#include <stdio.h>")
    w("#include <unistd.h>")
    w("int d[1000000000]={};")
    w("int ptr=0;")
    w("int last=0;")
    w("void pc(int x){if(x!=last){putchar(x);fflush(stdout);}last=x;}")
    w("int main(){")
    for c in code:
        if c == ".":
            w("pc(d[ptr]);")
        elif c == ",":
            w("d[ptr]=getchar();")
        elif c == "<":
            w("ptr--;")
        elif c == ">":
            w("ptr++;")
        elif c == "+":
            w("d[ptr]++;")
        elif c == "-":
            w("d[ptr]--;")
        elif c == "[":
            w("while(d[ptr]){")
        elif c == "]":
            w("}")
    w("return 0;")
    w("}")

os.system("gcc bf.c -o bf -Ofast && ./bf")
