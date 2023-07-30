#include <stdio.h>

int main() {
	int t1, t2;
	scanf("%d %d", &t1, &t2);

	int res = 2;

	while (t1 >= t2) {
		int temp = t1 - t2;
		t1 = t2;
		t2 = temp;
		res++;
	}
	printf("%d\n", res);

	return 0;
}
