#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);

    double volume = 0.0;
    double len;

    for (int i = 0; i < n; i++) {
        scanf("%lf", &len); 
        volume += pow(len, 3);
    }

    double ans = pow(volume, 1.0 / 3);
    printf("%.6lf\n", ans);

    return 0;
}
