#include <stdio.h>
#define FILE_SIZE 1860000

int main() {
    long long int s;
    int cnt = 0;

    while (1) {
        cnt++;
        scanf("%lld", &s);
        
        if (s == 0) {
            break;
        }
        if (s % 2) {
            s = s / 2 + 1;
        } else {
            s /= 2;
        }
        s += s / 2;
        
        printf("File #%d\n", cnt);
        printf("John needs %lld floppies.\n", (s + FILE_SIZE - 1) / FILE_SIZE);
        printf("\n");
    }

    return 0;
}
