#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);
    
    for (int k = 0; k < n; k++) {
        char x[20], y[20];
        scanf("%s %s", x, y);
        
        int lst[20];
        for (int i = 0; i < strlen(x); i++) {
            if ((int)x[i] > (int)y[i]) {
                lst[i] = 26 - ((int)x[i] - (int)y[i]);
            } else {
                lst[i] = (int)y[i] - (int)x[i];
            }
        }
        printf("Distances: ");
        for (int i = 0; i < strlen(x); i++) {
            printf("%d ", lst[i]);
        }
        printf("\n");
    }
    return 0;
}
