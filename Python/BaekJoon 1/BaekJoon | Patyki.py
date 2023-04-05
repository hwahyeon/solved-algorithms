lst = sorted(map(int, input().split()))
if lst[0] == lst[1] == lst[2]:
    print(2)
elif lst[0]**2 + lst[1]**2 == lst[2]**2:
    print(1)
else:
    print(0)
