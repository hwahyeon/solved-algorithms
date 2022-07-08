n = int(input())
for _ in range(int(input())):
    m, a = map(int, input().split())
    n -= m * a
print("Yes") if n == 0 else print("No")
