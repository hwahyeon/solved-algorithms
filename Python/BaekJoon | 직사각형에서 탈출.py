x, y, w, h = map(int, input().split())
lst = []
lst.append(x)
lst.append(y)
lst.append(abs(x-w))
lst.append(abs(y-h))
print(min(lst))
