#include <stdio.h>

int main() {
    int N, A, B, S;
    scanf("%d %d %d", &N, &A, &B);
    
    S = (N > B ) ? N : B;
    
    if (A == S) {
        printf("Anything\n");
    } else if (A > S) {
        printf("Subway\n");
    } else {
        printf("Bus\n");
    }
    
    return 0;
}
