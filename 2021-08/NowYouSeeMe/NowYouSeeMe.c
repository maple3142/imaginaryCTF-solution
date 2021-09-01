#include <stdio.h>

void fix_bytes(char *bytes, size_t szBytes)
{
    for (size_t i = 0 ; i < szBytes - 1; i++)
    {
        for (size_t ch = 0 ; ch < szBytes - i - 1; ch++)
        {
            if (bytes[ch] > bytes[ch + 1])
            {
                bytes[ch] = bytes[ch] ^ bytes[ch + 1];
                bytes[ch + 1]   =  bytes[ch] ^ bytes[ch + 1];
                bytes[ch] =  bytes[ch] ^ bytes[ch + 1];
            }
        }
    }
}

void merge_bytes(char *bytes, char *key)
{
    while (*bytes)
    {
        *bytes++ = *bytes ^ *key++;
    }
}

void deprecated(char *dest, char *src)
{
    while(*dest++ = *src++);
}

int main (int argc, char**argv)
{
    char *encrypted_flag = "P67ANY$QU3STV0IC25!WM14\0";
    char *magic = "HGDWIFkviEp$!zc$9!!xg#$\0";
    char encrypted_message[] = {7, 7, 65, 94, 88, 37, 117, 117, 67, 40, 8, 31, 72, 16, 29, 7, 84, 16, 27, 27, 82, 15, 92, 0};
    char temp[26];

    deprecated(temp, encrypted_flag);
    fix_bytes(temp, 23);
    merge_bytes(temp, magic);

    puts(temp);

    fix_bytes(temp, 23);
    merge_bytes(temp, encrypted_message);

    puts(temp);
    return(0);
}
