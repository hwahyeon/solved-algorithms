a, b = map(int, input().split())
lst = [int(str(a*i)[::-1]) for i in range(1, b+1)]
print(max(lst))
