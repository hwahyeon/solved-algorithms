#include <stdio.h>

int main() {
    while (1) {
        int cnt = 1;
        double c, len = 0;
        
        scanf("%lf", &c);
        
        if (c == 0.0)
            break;
        for (int i = 1;; i++) {
            len += 1.0 / (i + 1);
            
            if (len >= c) {
                cnt = i;
                break;
            }
        }
        printf("%d card(s)\n", cnt);
    }
    return 0;
}
