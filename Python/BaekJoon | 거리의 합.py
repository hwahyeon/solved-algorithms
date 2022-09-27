n = input()
r = 0
l = list(map(int, input().split()))
for i in range(0, len(l)):
    for j in range(i, len(l)):
        r += abs(l[i]-l[j])
print(r*2)
