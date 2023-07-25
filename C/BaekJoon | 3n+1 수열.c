#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int i = 1;
    while (n != 1) {
        if (n % 2) {
            n = 3 * n + 1;
        } else {
            n = n / 2;
        }
        i++;
    }
    printf("%d\n", i);

    return 0;
}
