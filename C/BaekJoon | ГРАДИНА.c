#include <stdio.h>

int main() {
    int w1, h1, w2, h2;
    scanf("%d", &w1);
    scanf("%d", &h1);
    scanf("%d", &w2);
    scanf("%d", &h2);

    printf("%d\n", 4 + 2 * (w1 > w2 ? w1 : w2) + 2 * (h1 + h2));

    return 0;
}
