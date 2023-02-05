#include <stdbool.h>

bool validateDigits(int *sudokuDigits)
{
    for (int i = 1; i < 10; i++) {
        if (sudokuDigits[i] != 1) return false;
        sudokuDigits[i] = 0;
    }
    return true;
}

bool validateSudoku(const int board[9][9])
{
    int sudokuDigits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for (int y = 0; y < 9; y++) {
        for (int x = 0; x < 9; x++) {
            sudokuDigits[board[x][y]]++;
        }
        if (!validateDigits(sudokuDigits)) return false;
    }
    for (int x = 0; x < 9; x++) {
        for (int y = 0; y < 9; y++) {
            sudokuDigits[board[x][y]]++;
        }
        if (!validateDigits(sudokuDigits)) return false;
    }
    for (int k = 0; k < 9; k++) {
        for (int i = 0; i < 9; i++) {
            sudokuDigits[board[k / 3 * 3 + i / 3][k % 3 * 3 + i % 3]]++;
        }
        if (!validateDigits(sudokuDigits)) return false;
    }
    return true;
}
