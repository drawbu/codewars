#include <stddef.h>

unsigned char *data_reverse(unsigned char *rdata, const unsigned char *data, size_t nblk)
{
    for (int i = 0; i < nblk; i++)
        for (int j = 0; j < 8; j++)
            rdata[i * 8 + j] = data[(nblk - 1 - i) * 8 + j];
    return rdata;
}
