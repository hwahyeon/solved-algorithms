#include <stdio.h>
#include <stdlib.h>

int main() {
    char s;
    scanf("%c", &s);
    
    printf("%d\n", abs(s - 'I') + 84);

    return 0;
}
