#include <stdio.h>

int main() {
    int n, od = 0, ev = 0;
  
    scanf("%d", &n);
    
    int l[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &l[i]);
    }

    for (int i = 0; i < n; i++) {
        if (l[i] % 2 == 0) {
            ev++;
        } else {
            od++;
        }
    }

    if (od < ev) {
        printf("Happy\n");
    } else {
        printf("Sad\n");
    }

    return 0;
}
