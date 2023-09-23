#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    if (n >= 8) {
        printf("%d\n", n - 7);
    } else {
        printf("%d\n", m + 7);
    }

    return 0;
}
