#include <stdio.h>
#include <stdlib.h>

long test(int a1)
{
    int i = 0;
    if (a1 == 1)
    {
        return 0;
    }
    for (i = 2; i < a1 - 1; ++i)
    {
        if (!(a1 % i))
        {
            return 0;
        }
    }
    return 1;
}
long next(long a1)
{
    int j;
    unsigned long v4;
    long v5;
    int i;
    for (i = 0; i <= 7; ++i)
    {
        v5 = 0;
        v4 = a1;
        for (j = 0; j <= 7; ++j)
        {
            if (test(j + 1))
                v5 ^= v4 & 1;
            v4 >>= 1;
        }
        a1 = (v5 << 7) + (a1 >> 1);
    }
    return a1;
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        return 1;
    }
    int n = atoi(argv[1]);
    long val = 2;
    for (int i = 0; i < n; i++)
    {
        val = next(val);
        printf("0x%02x, ", val);
    }
    return 0;
}
