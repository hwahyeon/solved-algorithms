#include <stdio.h>
 
int main() {
    int n, k = 0, t = 0;
    scanf("%d", &n);
    while (n != 0) {
        k++;
        
        if (n < k) {
            k = 1;
        }
        n -= k;
        t++;
    }
    printf("%d\n", t);
    
    return 0;
}
