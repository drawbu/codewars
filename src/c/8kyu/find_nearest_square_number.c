int sq(int n)
{
    return n * n;
}

int nearest_sq(int n)
{
    int i = 1;

    while (1) {
        if (sq(i) >= n) 
            return (sq(i) - n < n - sq(i - 1)) ? sq(i) : sq(i - 1);
        i++;
    }
}
