#include <stdio.h>

int main() {
    long long N, d;
    scanf("%lld", &N);
    scanf("%lld", &d);

    if (N <= 5) {
        for (long long i = 0; i < N - 1; i++) {
            d = !d;
            printf("%lld\n", d);
        }
    } else {
        printf("Love is open door\n");
    }

    return 0;
}
