#include <stdio.h>

int main() {
    long long l, t;
    scanf("%lld", &l);
    scanf("%lld", &t);

    long long diff = 2 * t - l;
    printf("%lld\n", diff);

    return 0;
}
