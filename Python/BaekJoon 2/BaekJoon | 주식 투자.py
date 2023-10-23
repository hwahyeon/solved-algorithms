import sys
r = sys.stdin.readline

for _ in range(int(r())):
    s = 0
    for _ in range(int(r())):
        m = max(map(int, r().split()))
        if m > 0:
            s += m
    print(s)
