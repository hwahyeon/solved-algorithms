def can_boil_same(boil_ints):
    s_max = 0
    e_min = 1000
    for s, e in boil_ints:
        s_max = max(s_max, s)
        e_min = min(e_min, e)
    return "edward is right" if s_max > e_min else "gunilla has a point"

N = int(input())
ints = [tuple(map(int, input().split())) for _ in range(N)]

print(can_boil_same(ints))
