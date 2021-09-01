#include <stdio.h>
#include <stdlib.h>

int password = 0x65706f6e;

int main() {
    setbuf(stdout, NULL);
    printf("The password is at %p\n\n", &password);
    puts("What's your name?");
    char name[100];
    fgets(name, 100, stdin);
    printf("Hi, ");
    printf(name);
    printf("!\n");
    if (password == 0x87654321) {
        puts("Winner!");
        FILE* f = fopen("flag.txt", "r");
        fscanf(f, "%s", name);
        fclose(f);
        puts(name);
    } else {
        printf("Sorry, you entered the password %08x...\n", password);
    }
}