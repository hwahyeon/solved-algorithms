#include <stdio.h>

int main() {
    long long x, k, a;
    scanf("%lld %lld %lld", &x, &k, &a);
    if (x % (k + a) < k)
        printf("1");
    else
        printf("0");

    return 0;
}
