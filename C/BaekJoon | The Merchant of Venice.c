#include <stdio.h>

int main() {
    int n, s, d, t, ans;
    
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        scanf("%d %d %d", &n, &s, &d);
        ans = 0;
        
        for (int j = 0, a, b; j < n; j++) {
            scanf("%d %d", &a, &b);
            
            if (s * d >= a) {
                ans += b;
            }
        }
        printf("Data Set %d:\n%d\n\n", i, ans);
    }
    return 0;
}
