a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

print(max(a2-a1, 0) + max(b2-b1, 0) + max(c2-c1, 0))
