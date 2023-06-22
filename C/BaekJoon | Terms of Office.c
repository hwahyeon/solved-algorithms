#include <stdio.h>

int X, Y;

int main() {
    scanf("%d %d", &X, &Y);
    while (X <= Y) {
        printf("All positions change in year %d\n", X);
        X += 60;
    }
    return 0;
}
