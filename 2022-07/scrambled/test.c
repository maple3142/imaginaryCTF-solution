#include <stdio.h>
#include <stdlib.h>


void scramble(char* buf, int ln){
    for(int i=0;i<ln;i++){
        int a = rand()%ln;
        int b = rand()%ln;
        char tmp = buf[a];
        buf[a] = buf[b];
        buf[b] = tmp;
    }
}
int main(){
    // printf("%x", rand());
    // return 0;
    char buf[0x10];
    for(int i=0;i<0x10;i++){
        buf[i]=i;
    }
    scramble(buf,0x10);
    for(int i=0;i<0x10;i++){
        printf("%.2x",buf[i]);
    }
}
