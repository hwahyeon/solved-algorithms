#include <stdio.h>

int main() {
    char input[4];
    
    scanf("%s", input);
    
    switch(input[0]) {
        case 'N':
            printf("North London Collegiate School\n");
            break;
        case 'B':
            printf("Branksome Hall Asia\n");
            break;
        case 'K':
            printf("Korea International School\n");
            break;
        case 'S':
            printf("St. Johnsbury Academy\n");
            break;
    }
    
    return 0;
}
