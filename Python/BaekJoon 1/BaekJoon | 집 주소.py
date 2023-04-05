dist = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    n = input()
    if n == '0':
        break
    else:
        res = len(n)+1
        for i in n:
            res += dist[int(i)]
        print(res)
