#include <stdio.h>

int main() {
    int b[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &b[i]);
    }
    int res = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &b[i]);
        for (int j = i + 1; j < 10; j++) {
            res ^= (b[i] || b[j]);
            for (int k = j + 1; k < 10; k++){
                res ^= (b[i] || b[j] || b[k]);
            }
        }
    }
    printf("%d\n", res);
    
    return 0;
}
