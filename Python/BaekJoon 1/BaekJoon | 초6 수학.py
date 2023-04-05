import sys
input = sys.stdin.readline

def GCD(x, y):
    while y > 0:
        x, y = y, x%y
    return x

def LCM(x, y):
    return (x*y)//GCD(x, y)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(LCM(a, b), GCD(a, b))
