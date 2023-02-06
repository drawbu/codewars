#include <math.h>

typedef struct Point {
    double x;
    double y;
} point;

double distance_between_points(point a, point b)
{
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}
