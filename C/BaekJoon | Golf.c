#include <stdio.h>

char* getName(int p, int s) {
    int diff = p - s;
    if (diff == 1) return "Birdie.\n";
    if (diff == -1) return "Bogey.\n";
    if (diff == 2 && s == 1) return "Hole-in-one.\n";
    if (diff == 2) return "Eagle.\n";
    if (diff == 3) return "Double eagle.\n";
    if (diff == 0) return "Par.\n";
    return "Double Bogey.\n";
}

int main() {
int p, s, cnt = 0;
while (1) {
    cnt++;
    scanf("%d %d", &p, &s);
    
    if (p == 0 && s == 0) {
        break;
    }
    printf("Hole #%d\n", cnt);
    printf("%s\n", getName(p, s));
    }
    return 0;
}
