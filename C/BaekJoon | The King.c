#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compare_desc(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

int compare_abs_desc(const void* a, const void* b) {
    return (abs(*(int*)b) - abs(*(int*)a));
}

int main() {
    int n, e; // changed cntSons to n and exponent to e
    scanf("%d %d", &n, &e);

    int pos[n], neg[n]; // changed posPotential to pos and negPotential to neg
    int pSize = 0, nSize = 0; // changed posSize to pSize and negSize to nSize
    for (int i = 0; i < n; i++) {
        int val; // changed potential to val
        scanf("%d", &val);
        if (val > 0) pos[pSize++] = val;
        else neg[nSize++] = val;
    }

    qsort(pos, pSize, sizeof(int), compare_desc);
    qsort(neg, nSize, sizeof(int), compare_abs_desc);

    int maxWin = 0; // changed maxChanceWin to maxWin
    for (int i = 0; i < pSize; i++)
        maxWin += pow(pos[i], e);

    if (e % 2 == 0) {
        for (int i = 0; i < nSize; i++)
            maxWin += pow(neg[i], e);
    }

    printf("%d\n", maxWin);

    return 0;
}
