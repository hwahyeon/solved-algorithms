n, k = map(int, input().split())
A = list(map(int, input().split()))

s = 0
for i in A:
    if i%2 == 0:
        s += i/2
    else:
        s += int(i/2) + 1

print("YES") if n <= s else print("NO")
