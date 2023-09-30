#include <stdio.h>

int main() {
    int W, H;
    double area;

    scanf("%d %d", &W, &H);

    area = W * H / 2.0;

    printf("%.1f\n", area);

    return 0;
}
