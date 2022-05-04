#include <stdio.h>

// gcc sc.c -o sc -z execstack

int main() {
  char buf[512];
  int (*sc)() = (int(*)())buf;
  setvbuf(stdin, NULL, 2, 0);
  setvbuf(stdout, NULL, 2, 0);
  puts("What is your shellcode?");
  fgets(buf, 512, stdin);
  sc();
}
