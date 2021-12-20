import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
K = math.ceil(A/C)
M = math.ceil(B/D)
print(L-K) if K > M else print(L-M)
