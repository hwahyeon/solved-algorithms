#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int a, b, c, d;
    int cnt;

    while (1) {
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if (a == 0 && b == 0 && c == 0 && d == 0) {
            break;
        }
        cnt = 0;
        while (!(a == b && b == c && c == d)) {
            int tmp1 = abs(a - b);
            int tmp2 = abs(b - c);
            int tmp3 = abs(c - d);
            int tmp4 = abs(d - a);
            a = tmp1;
            b = tmp2;
            c = tmp3;
            d = tmp4;
            cnt += 1;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
