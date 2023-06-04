#include <stdio.h>

int main(void) {
	while (1) {
		int a, b;
		scanf("%d %d", &a, &b);

		if (a == 0 && b == 0){
			break;
		}

		int group = (a - b) / 2 - (a - b) % 2;
		if (group < 0){
			group = 0;
		}

		int group_trd = 0;
		if (a - b > 1){
			group_trd = (a - b) % 2;
		}

		printf("%d %d\n", group, group_trd);
	}

	return 0;
}
