#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void run() {
    char name[16];
    char message[128];
    for (int i = 0; i < 5; i++) {
        printf("What message would you like to leave?\n");
        gets(&message[0]);
        message[127] = '\0';
        if (strchr(message, '%')) {
            printf("I don't like math, go away...\n");
            abort();
        }
        printf("And what name do you wish to sign it with?\n");
        gets(&name[0]);
        name[15] = '\0';
        printf("So %s, are you sure you want to submit the following message?\n", name);
        printf(message);
        printf("\n[y/n] ");
        if (getchar() == 'y') {
            getchar();
            return;
        }
        getchar(); // eat the newline
    }
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    printf("Welcome, leave your fractions at the door, please.\n");
    printf("Could you fill in the guestbook before you come further?\n");
    run();
}
