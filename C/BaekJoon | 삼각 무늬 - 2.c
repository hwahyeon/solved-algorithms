#include <stdio.h>

int main() {
    long long a, b;
    int n;
    scanf("%lld", &n);

    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &a, &b);
        printf("%lld\n", (a / b) * (a / b));
    }
    
    return 0;
}
