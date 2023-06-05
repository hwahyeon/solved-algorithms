#include <stdio.h>

int main() {
    int k, q, t;
    int time = 0;
    char r;
    
    scanf("%d %d", &k, &q);
    
    while (q--) {
        scanf("%d %c", &t, &r);
        
        time += t;
        
        if (time >= 210) {
            printf("%d\n", k);
            break;
        }
        if (r == 'T') {
            k++;
            if (k == 9) {
                k = 1;
            }
        }
    }
    return 0;
}
