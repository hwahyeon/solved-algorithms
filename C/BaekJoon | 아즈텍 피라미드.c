#include <stdio.h>

int main() {
    int n;
    int h = 0, az = 0;

    scanf("%d", &n);

    while (az <= n) {
        az += 2*h*h + 2*h + 1;
        h++;
    }
    printf("%d\n", h - 1);

    return 0;
}
