n, a, b = map(int, input().split())
for _ in range(n):
    print("NE") if (a**2 + b**2)**0.5 < int(input()) else print("DA")
