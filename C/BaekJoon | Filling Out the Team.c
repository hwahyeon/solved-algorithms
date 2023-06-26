#include <stdio.h>

int main() {
    while (1) {
        float sp, wt, st;
        int p = 0;
        scanf("%f %f %f", &sp, &wt, &st);
        if (sp == 0 && wt == 0 && st == 0)
            break;
        if (sp <= 4.5 && wt >= 150 && st >= 200) {
            p = 1;
            printf("Wide Receiver ");
        }
        if (sp <= 6.0 && wt >= 300 && st >= 500) {
            p = 1;
            printf("Lineman ");
        }
        if (sp <= 5.0 && wt >= 200 && st >= 300) {
            p = 1;
            printf("Quarterback ");
        }
        if (p == 0) {
            printf("No positions ");
        }
        printf("\n");
    }
    return 0;
}
