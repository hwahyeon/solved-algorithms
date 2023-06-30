#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int iMon, iYrs, sMon, sYrs;
        scanf("%d %d %d %d", &iMon, &iYrs, &sMon, &sYrs);

        double eit = 0.0;
        if (iYrs == sYrs)
            eit += 0.5 * (sMon - iMon) / ((12.0 - iMon) + 1);
        else
            eit += 0.5 + (sYrs - iYrs - 1) + ((sMon - 1) / 12.0);

        printf("%.4f\n", eit);
    }
    return 0;
}
