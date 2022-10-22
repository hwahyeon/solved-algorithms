l = list(map(int, input().split()))
l.sort()
if l[2] - l[1] == l[0]:
    print(1)
elif l[2] / l[1] == l[0]:
    print(2)
else:
    print(3)
