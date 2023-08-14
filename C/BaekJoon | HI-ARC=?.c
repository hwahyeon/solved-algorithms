#include <stdio.h>

int main() {
    int H, I, A, R, C;
    scanf("%d %d %d %d %d", &H, &I, &A, &R, &C);

    int result = (H * I) - (A * R * C);
    printf("%d\n", result);

    return 0;
}
