#include <stdio.h>

int main(void){
	int n, m, k;
	long long res;
	
	scanf("%d %d %d", &n, &m, &k);

	if (m < k) {
		res = n * m;
	}
	else {
		res = n * ((k - 1) + m / k);
	}

	printf("%lld\n", res);

	return 0;
}
