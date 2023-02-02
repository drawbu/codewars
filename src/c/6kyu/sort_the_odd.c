#include <stdlib.h>

void sort_array(size_t n, int arr[n]) 
{
    int tmp;

	for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) continue;
        for (int j = 0; j < i; j++) {
            if (arr[j] % 2 == 0) continue;
            if (arr[j] > arr[i]) {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}
