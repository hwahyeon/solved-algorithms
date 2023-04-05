A, B = map(int, input().split())
A -= 1
B -= 1
print(abs(B//4 - A//4) + abs(A%4 - B%4))
