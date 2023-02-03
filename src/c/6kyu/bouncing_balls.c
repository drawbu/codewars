int bouncingBall(double h, double bounce, double window) {
    int result = -1;
    double last = h;

    if (h <= 0) return -1;
    if (bounce <= 0 || bounce >= 1) return -1;
    if (window >= h) return -1;
    while (last > window) {
        result += 2;
        last *= bounce;
    }    
    return result;
}
