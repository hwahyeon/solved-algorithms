for _ in range(int(input())):
    r = list(map(int, input()))[::-1]
    for i in range(len(r)-1):
        if r[i] > 4:
            r[i+1] += 1
            r[i] = 0
    print(r[::-1][0] * (10 ** (len(r)-1)))
