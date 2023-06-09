#include <stdio.h>
#include <string.h>

int main() {
  char encry[100];
  scanf("%s", encry);

  char r[100] = "";
  int i = 0;
  while (1) {
    if (i == strlen(encry) - 1)
      break;

    r[strlen(r)] = encry[i];
    i += encry[i] - 'A' + 1;
  }

  r[strlen(r)] = encry[strlen(encry) - 1];
  printf("%s\n", r);

  return 0;
}
