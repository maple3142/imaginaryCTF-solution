#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main() {
    int64_t num;
    int64_t buf[32];

    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);

    printf("Welcome to my More Secure Flag Storage!\n");
    printf("In fact, it is so secure, I'll even tell you where I am: %p\n", main);
    printf("How many numbers do you want to submit?\n> ");
    scanf("%ld", &num);

    if(num > 32) {
        printf("Sorry, but we don't have that much storage capacity :(");
        exit(1);
    }

    while(num--) {
        printf("Enter the next number: ");
        scanf("%ld", &buf[num]);
    }

    if(num == 64) { // You will never get my flag >:)
        char buf[0x50];
        FILE *f;

        f = fopen("flag.txt", "r");
        fgets(buf, 0x50, f);
        puts(buf);
        fclose(f);
    }

    return 0;
}
