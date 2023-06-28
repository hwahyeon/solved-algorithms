#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int a, x, b, y, T;
    scanf("%d", &a);
    scanf("%d", &x);
    scanf("%d", &b);
    scanf("%d", &y);
    scanf("%d", &T);

    int A = a + max(T - 30, 0) * x * 21;
    int B = b + max(T - 45, 0) * y * 21;

    printf("%d %d\n", A, B);
    return 0;
}
