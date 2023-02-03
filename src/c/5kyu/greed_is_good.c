int score(const int dice[5]) {
    int score = 0;
    int count[7] = {0, 0, 0, 0, 0, 0, 0};

    for (unsigned i = 0; i < 5; i++)
        count[dice[i]]++;
    // Three 1's => 1000 points
    score += count[1] / 3 * 1000;
    // Three 6's =>  600 points
    score += count[6] / 3 * 600;
    // Three 5's =>  500 points
    score += count[5] / 3 * 500;
    // Three 4's =>  400 points
    score += count[4] / 3 * 400;
    // Three 3's =>  300 points
    score += count[3] / 3 * 300;
    // Three 2's =>  200 points
    score += count[2] / 3 * 200;
    // One   1   =>  100 points
    score += count[1] % 3 * 100;
    // One   5   =>   50 point
    score += count[5] % 3 * 50;
    return score;
}
