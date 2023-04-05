num = int(input())
for i in range(num):
    ox = (list(input()))
    sco = 0
    c = 1
    for i in ox:
        if i == 'O':
            sco += c
            c += 1
        else:
            c = 1
    print(sco)
