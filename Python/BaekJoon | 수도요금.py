A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = P * A
if P > C:
    Y = B + (P - C) * D
else:
    Y = B

print(X) if X < Y else print(Y)
