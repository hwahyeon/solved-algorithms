#include <stdio.h>

int cnt[128] = {0};
char c;

int main() {
	while (scanf("%c", &c) != EOF) {
		cnt[c]++;
	}

	printf("%d\n", cnt['B'] / 2 + cnt['C'] / 2);

	return 0;
}
