#include <stdio.h>

int main() {
    int ra = 0, rb = 0, rc = 0;
    int n, a, b, c;
    
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &a, &b, &c);
        ra += a;
        rb += b;
        rc += c;
        
        if (ra < 30 || rb < 30 || rc < 30) {
            printf("NO\n");
        } else {
            int m = (ra < rb && ra < rc) ? ra : (rb < rc) ? rb : rc;
            printf("%d\n", m);
            ra -= m;
            rb -= m;
            rc -= m;
        }
    }
    
    return 0;
}
