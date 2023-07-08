#include <stdio.h>

int main() {
    float M, S, G;
    scanf("%f %f %f", &M, &S, &G);

    float A, B;
    scanf("%f %f", &A, &B);

    float L, R;
    scanf("%f %f", &L, &R);

    float lw = L / A;
    float rw = R / B;

    int lv = M / G;
    if ((int)M % (int)G != 0){
        lv += 1;        
    }

    int rv = M / S;
    if ((int)M % (int)S != 0){
        rv += 1;       
    }

    if (lv + lw < rv + rw){
         printf("friskus\n");
    } else {
         printf("latmask\n");
    }
  
    return 0;
}
