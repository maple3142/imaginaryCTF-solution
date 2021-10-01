#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

#include <sys/mman.h>

#define BUFLEN 1024
#define MAX_OUTPUT 0x10000
#define RAM_SIZE 0x200

int main() {
    char userinput[BUFLEN];
    char flag[100];

    // Read the flag file
    FILE *f = fopen("flag.txt", "r");
    if(!f) exit(2);
    int len = fread(flag, 1, 100, f);
    flag[len] = 0;
    fclose(f);

    // Set stdin/stdout unbuffered
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    // Set up VM memory
    unsigned char *ram = (unsigned char*) mmap(NULL, RAM_SIZE, 
            PROT_READ | PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0);
    char *out = (char*) mmap(NULL, MAX_OUTPUT, PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0);
    int x = 0, y = 0, syscall_code = 0, exit_code = 0;
    bool running = true;
    bool debug = true;

    while(running) {
        // Read user input
        memset(userinput, 0, BUFLEN);
        fgets(userinput, BUFLEN, stdin);
        bool invalid = false;
        int perc = 0, ast = 0;

        // Check that we don't use arbitrary arguments
        char *cur = userinput;
        for(int i = 0; i < BUFLEN; i++) {
            if(*cur == '%') perc++;
            if(*cur == '$') invalid |= *(cur-2) != '%' && *(cur-2) != '*'; // can only use one digit arg ==> 9 args
            if(*cur == '*') ast++;
            cur++;
        }
        if(perc > 7 || ast > 2) invalid = true;

        if(!invalid) {
            snprintf(out, MAX_OUTPUT, userinput, 
                    "",                 // empty string ==> %<num>s or %*s allow one to precisely print that many chars
                    *ram, ram, &ram,    // ram deref, ram (the ptr) and ptr to the ptr, to access and modify memory values
                    x, &x,              // a register
                    y, &y,              // another register
                    &syscall_code       // if the program should exit / the exit code with it
                );

            // Check if the VM called a "syscall"
            if(syscall_code) {
                switch(syscall_code) {
                    case 1: // getchar ==> "read"
                        *ram = (unsigned char)getchar();
                        break;
                    case 2: // putchar ==> "write"
                        putchar(*ram);
                        break;
                    case 0xFE:
                        debug = true;
                        break;
                    case 0xFF: // set exit code ==> "exit"
                        exit_code = *ram;
                        running = false;
                        break;
                    case 69:
                        if(x == 42 && y == 0x1337 && !strcmp((char*)ram, "gimmeflagpls")) {
                            printf("You earned your flag: %s\n", flag);
                            running = false;
                        }
                        break;
                    default:
                        printf("Unknown syscall: %d\n", (int)syscall_code);
                }
                syscall_code = 0;
            }

            if(debug) {
                // Print status
                printf("Current status:\n\tx=0x%.08x\ty=0x%.08x\tsyscall=0x%.02x\n\t*ram=0x%.02x\tram=0x%.08x\n", 
                        x, y, syscall_code, *ram, (int)ram);
                printf("Addr: &x=%p, &y=%p\n, ram=%p", &x, &y, ram);
            }
        }
    }

    // Clean up
    munmap(ram, RAM_SIZE);
    munmap(out, MAX_OUTPUT);

    return exit_code;
}
