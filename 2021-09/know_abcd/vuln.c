#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char buf[64];
    int password;
} user_data;

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    user_data data;

    puts("Welcome to my secure flag storage");
    printf("Please Enter the secret password: ");
    scanf("%d%*c", &data.password);

    if(data.password > 1000) {
        puts("It's not that large :(");
        exit(1);
    }

    puts("Anything you'd like to improve on our service?");
    gets(data.buf);
    puts("Thanks for your feedback :)");

    if(data.password == 0x61626364) {
        char buf[0x50];
        FILE *f;

        f = fopen("flag.txt", "r");
        fgets(buf, 0x50, f);
        puts(buf);
        fclose(f);
    }

    exit(0);
}
