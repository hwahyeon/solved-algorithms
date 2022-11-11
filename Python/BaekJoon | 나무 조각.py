l = list(map(int, input().split()))

def cycle(l):
    for i in range(4):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            print(' '.join(map(str, l)))

while not (l[0] < l[1] < l[2] < l[3] < l[4]):
    cycle(l)
