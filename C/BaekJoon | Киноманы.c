#include <stdio.h>

int main() {
    int t1, e1, f1;
    int t2, e2, f2;
    int r1, r2;

    scanf("%d %d %d", &t1, &e1, &f1);
    scanf("%d %d %d", &t2, &e2, &f2);

    r1 = 3 * t1 + 20 * e1 + 120 * f1;
    r2 = 3 * t2 + 20 * e2 + 120 * f2;

    if (r1 < r2) {
        printf("Mel\n");
    } else if (r1 > r2) {
        printf("Max\n");
    } else {
        printf("Draw\n");
    }

    return 0;
}
