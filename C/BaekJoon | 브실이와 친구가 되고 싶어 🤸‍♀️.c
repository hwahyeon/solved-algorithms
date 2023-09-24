#include <stdio.h>

int main() {
    int A, B, K, X;
    scanf("%d %d %d %d", &A, &B, &K, &X);

    int ppl = 0;
    for(int i = K - X; i < K + X + 1; i++) {
        if(i < A || i > B) continue;
        ppl++;
    }

    if(ppl == 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", ppl);

    return 0;
}
