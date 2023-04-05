N = input()
lst = []
if '0' not in N:
    print(-1)
else:
    for i in N:
        lst.append(int(i))
    if sum(lst)%3 != 0:
        print(-1)
    else:
        print(''.join(sorted(N, reverse=True)))
