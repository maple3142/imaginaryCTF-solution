#include <stdio.h>

extern gets;

struct contrived_chall {
  char lolololol[1000];
  long code;
};

void (*lolol)(char*) = &puts;
void (*lololol)(char*) = &gets;

int main() {
  struct contrived_chall lol;
  setvbuf(stdin, NULL, 2, 0);
  setvbuf(stdout, NULL, 2, 0);
  lolol("[EXCEPTION] Angle Brackets unterminated.");
  lololol(lol.lolololol);
  if (lol.code == 0x3e3e3e3e3e3e3e3e) {
    FILE *fp;
    fp = fopen("flag.txt", "r");
    fscanf(fp, "%s", lol.lolololol);
    lolol(lol.lolololol);
  }
  lolol("[MESSAGE] Exception unresolved. Exiting.");
}
