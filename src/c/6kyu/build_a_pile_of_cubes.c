long long findNb(long long m)
{
    long long n = 0;

    while (m > 0) {
        n++;
        m -= n * n * n;
    }
    return (m == 0) ? n : -1;
}
