#include <stdio.h>
#include <string.h>

int main(){
    int n = 0x401070;
    // printf("%4635c%8$hn", 1,2,3,4,5,6,7,&n);
    printf("%*9$c%8$hn", 1,2,3,4,5,6,7,&n,0x121b,'a');
    printf("\n%x\n",n);
    return 0;
}
