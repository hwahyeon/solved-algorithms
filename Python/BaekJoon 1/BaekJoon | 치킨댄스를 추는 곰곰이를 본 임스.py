N = int(input())
A, B = map(int, input().split())
A = A//2
print(min(A+B, N))
