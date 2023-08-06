#include <stdio.h>

int main(void) {
    int n, a, b;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);
        long long res = ((long long)(b - a + 1) * (a + b)) / 2;
        printf("Scenario #%d:\n", i + 1);
        printf("%lld\n\n", res);
    }

    return 0;
}
