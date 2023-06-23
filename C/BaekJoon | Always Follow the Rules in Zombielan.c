#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int q, r, rule;
    scanf("%d", &q);
    getchar();
    char** quotes = (char**)malloc(q * sizeof(char*));
    
    for (int i = 0; i < q; i++) {
        quotes[i] = (char*)malloc(100 * sizeof(char));
        fgets(quotes[i], 100, stdin);
        quotes[i][strlen(quotes[i]) - 1] = '\0';
    }

    scanf("%d", &r);
    for (int i = 0; i < r; i++) {
        scanf("%d", &rule);
        if (rule > 0 && rule <= q)
            printf("Rule %d: %s\n", rule, quotes[rule - 1]);
        else
            printf("Rule %d: No such rule\n", rule);
    }

    // 동적 할당 메모리 해제
    for (int i = 0; i < q; i++) {
        free(quotes[i]);
    }
    free(quotes);

    return 0;
}
