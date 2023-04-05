import sys
A, B = 0, 0

for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        A += 1
    elif b > a:
        B += 1
print(A, B)
