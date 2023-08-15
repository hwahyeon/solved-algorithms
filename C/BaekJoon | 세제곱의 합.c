#include <stdio.h>

int main() {
    int n;
    long long r;

    scanf("%d", &n);

    r = (long long)n * (n + 1) / 2;
    printf("%lld\n", r);
    printf("%lld\n", r * r);
    printf("%lld\n", r * r);

    return 0;
}
