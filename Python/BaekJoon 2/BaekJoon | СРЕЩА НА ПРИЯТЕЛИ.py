def meet(l):
    start = max(l[0], l[2])
    end = min(l[1], l[3])

    return max(0, end - start + 1 - (l[4] in range(start, end + 1)))

print(meet(list(map(int, input().split()))))
