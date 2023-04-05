import math

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(math.factorial(M) // (math.factorial(N) * math.factorial(M - N)))
