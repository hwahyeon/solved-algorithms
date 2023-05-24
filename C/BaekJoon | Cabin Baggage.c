#include <stdio.h>

int main() {
    int n, r, i;
    float l, w, d, kg;

    scanf("%d", &n);
    
    r = 0;

    for (i = 0; i < n; i++) {
        scanf("%f %f %f %f", &l, &w, &d, &kg);
        if ((((l <= 56.0) && (w <= 45.0) && (d <= 25.0)) || (l + w + d <= 125.0)) && (kg <= 7.0)) {
            printf("1\n");
            r++;
        } else {
            printf("0\n");
        }
    }

    printf("%d\n", r);

    return 0;
}
