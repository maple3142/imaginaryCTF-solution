#include <stdio.h>
#include <string.h>

int main(){
    int n = 0x401070;
    printf("%1$78c", 'c');
    // printf("%*9$c%8$hn", 1,2,3,4,5,6,7,&n,(0xfL<<32)|0x121bL,'a');
    printf("\n%x\n",n);
    return 0;
}
