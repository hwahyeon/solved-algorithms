mn, mx = map(int, input().split())
lst = [True] * (mx-mn+1)

for i in range(2, int(mx**0.5)+1):
    sq = i*i
    while sq <= mx:
        idx = int(mn/sq) * sq
        for j in range(idx, mx+1, sq):
            if j >= mn:
                lst[j-mn] = False
        sq *= i

print(sum(lst))
