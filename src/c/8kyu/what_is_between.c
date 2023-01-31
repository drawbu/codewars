// https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/c

void between(int a, int b, int *integers)
{
    for (int i = 0; i < b - a + 1; i++)
        integers[i] = i + a;
}
