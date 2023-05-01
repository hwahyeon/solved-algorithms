while 1:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    r = 1
    for i in range(1, len(l), 2):
        r = r * l[i] - l[i+1]
    print(r)
