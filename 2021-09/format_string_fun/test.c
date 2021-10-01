#include <stdio.h>
#include <string.h>

int main() {
	char buf[256];
	memset(buf, 0, sizeof(buf));
	char *p = buf;
	printf("%p %p\n", p, &p);

	// must not use positional specifier, or it won't work
	printf("%c%c%c%c%c%c%c%c%c%c%244c%hhn %15$hhn\n", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, &p, p);

	// printf("%1$254c%12$hhn %13$p %15$p\n", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, &p, p);

	// printf("%1$254c%12$hhn %13$p %15$p\n", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, &p, p);
	// printf("%13$p %15$p\n", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, &p, p);

	// printf("%1$254c%12$hhnx%15$hhn\n", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, &p, p);
	printf("%p %p\n", p, &p);
	// *p = 15;
	for (int i = 0; i < 256; i += 8) {
		printf("%d %d %d %d %d %d %d %d\n", buf[i], buf[i + 1], buf[i + 2],
		       buf[i + 3], buf[i + 4], buf[i + 5], buf[i + 6], buf[i + 7]);
	}
}
