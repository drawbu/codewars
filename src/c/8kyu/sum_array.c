#include <stddef.h>

int sum_array(const int *values, size_t count)
{
    int sum = 0;
    for (unsigned int i = 0; i < count; i++)
        sum += values[i];
    return sum;
}
