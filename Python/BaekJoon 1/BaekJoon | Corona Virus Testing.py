g, p, t = map(int, input().split())

individual = g * p
group = g + t * p

if individual < group:
    print(1)
elif individual > group:
    print(2)
else:
    print(0)
