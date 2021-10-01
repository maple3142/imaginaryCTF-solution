#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main() {
    int64_t num;
    int64_t buf[2];

    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);

    printf("Welcome to my More Secure Flag Storage!\n");
    printf("In fact, it is so secure, I'll even tell you where I am: %p\n", main);
    printf("How many numbers do you want to submit?\n> ");
    scanf("%ld", &num);

    if(num > 2) { // budget was lowered because I kept losing my flags...
        printf("Sorry, but we don't have that much storage capacity :(");
        exit(1);
    }

    while(num--) {
        printf("Enter the next number: ");
        scanf("%ld", &buf[num]);
    }

    // You'll never get my flag if I do this :P
    if(num == 64) {
        FILE *f;
        char buf[8];

        f = fopen("/dev/urandom", "r");
        fgets(buf, 8, f);
        printf("Here have this: %p\n", (uint64_t*)buf);
        fclose(f);
    }

    return 0;
}
