#include <stdio.h>

int main() {
    long long int w, b;
    scanf("%lld %lld", &w, &b);

    if (w >= b)
        printf("%lld\n", b);
    else
        printf("%lld\n", w + 1);

    return 0;
}
