r = 0

for _ in range(int(input())):
    skate = list(map(int, input().split()))
    run = skate[:2]
    trick = skate[2:]

    run.sort(reverse=True)
    trick.sort(reverse=True)

    r = max(r, run[0] + sum(trick[:2]))

print(r)
