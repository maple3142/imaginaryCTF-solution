#include <stdio.h>

// w0152 scan
int wscan(char buf[], int n) {
    for (int i = 0; i < n; i++) {
        char c = getchar();
        if (c != '\n') {
            buf[i] = c;
        }
        else {
            return i;
        }
    }
}

int main() {
    char flag[64];
    char buf[32];
    setbuf(stdout, NULL);
    FILE *f = fopen("flag.txt", "r");
    fgets(flag, 64, f);
    fclose(f);
    puts("Enter something to be echoed");
    wscan(buf, 32);
    puts(buf);
    return 0;
}

