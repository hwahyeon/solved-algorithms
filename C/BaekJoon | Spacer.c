#include <stdio.h>

int abs(int x) {
    return (x < 0) ? -x : x;
}

int main() {
    int Z, N;
    char S[500004];
    scanf("%d", &Z);
    
    while (Z--) {
        int X = 0, Y = 0;
        
        scanf("%d %s", &N, S);
        
        for (int i = 0; i < N; i++) {
            if (S[i] == 'N')
                Y++;
            else if (S[i] == 'E')
                X++;
            else if (S[i] == 'W')
                X--;
            else if (S[i] == 'S')
                Y--;
        }
        printf("%d\n", abs(X) + abs(Y));
    }
    return 0;
}
