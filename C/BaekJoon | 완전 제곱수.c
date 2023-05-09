#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, cnt = 0;
    scanf("%d", &n);
    
    for (int i = 1; i < n; i++) {
        if (i * i - (i-1) * (i-1) > n) {
            break;
        }
        for (int j = 1; j <= i; j++) {
            if (i * i - j * j == n) {
                cnt += 1;
            }
        }
    }
    printf("%d", cnt);
    
    return 0;
}
