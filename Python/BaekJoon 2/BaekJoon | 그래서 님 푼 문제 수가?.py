N, M, K = map(int, input().split())

r1 = N - M * K if N - M * K > 0 else 0
r2 = N - M * (K - 1) - 1
print(r1, r2)
