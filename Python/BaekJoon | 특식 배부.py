n = int(input())
A, B, C = map(int, input().split())

print(min(A, n) + min(B, n) + min(C, n))
