#include <stdio.h>

int main() {
    int t, n, a, b;
    
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        printf("Case %d:\n", i+1);
        
        for (a = 1; a <= 6; a++) {
            for (b = a; b <= 6; b++) {
                if (a + b == n) {
                    printf("(%d,%d)\n", a, b);
                }
            }
        }
    }

    return 0;
}
