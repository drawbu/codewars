#include <stddef.h>

void pair_zeros(size_t a, const int array[a], size_t *r, int *results)
{
    int pair = 1;

    if (!a) return;
    for (unsigned long i = 0; i < a; i++) {
        if (array[i] == 0) {
            pair = !pair;
            if (pair) continue;
        }
        results[*r] = array[i];
        (*r)++;
    }
}
