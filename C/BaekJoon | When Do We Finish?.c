#include <stdio.h>

int main() {
    while (1) {
        char s[9], d[9];
        int h1, m1, h2, m2;

        scanf("%s %s", s, d);
        sscanf(s, "%d:%d", &h1, &m1);
        sscanf(d, "%d:%d", &h2, &m2);

        if (h1 == 0 && m1 == 0 && h2 == 0 && m2 == 0)
            break;

        int t = h1 * 60 + m1 + h2 * 60 + m2;
        int n = t / 60 / 24;
        int h = (t / 60) % 24;
        int m = t % 60;

        if (n > 0) {
            printf("%02d:%02d +%d\n", h, m, n);
        } else {
            printf("%02d:%02d\n", h, m);
        }
    }

    return 0;
}
