#include <stddef.h>
#include <stdio.h>

size_t count_pixels(size_t k) {
    size_t sum = 0;

    sum += 4 * (k - 1); // center
    if (!sum)
        sum = 1;
    sum += 4 * (k + 2) - 2; // borders
    return sum;
}
