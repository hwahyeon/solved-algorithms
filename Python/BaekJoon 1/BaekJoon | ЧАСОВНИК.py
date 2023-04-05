t1, m1, t2, m2 = map(int, input().split())
if (t1 * 60 + m1) > (t2 * 60 + m2):
    t2 += 24
res = (t2 * 60 + m2) - (t1 * 60 + m1)
print(res, res//30)
