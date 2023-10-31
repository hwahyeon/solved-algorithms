n, t = map(int, input().split())
tasks = 0
l = list(map(int, input().split()))
for i in l:
    if t >= i:
        t -= i
        tasks += 1
    else:
        print(tasks)
        break
if tasks == n: print(tasks)
