a, b = map(int, input().split())
max_num = max(a, b)
min_num = min(a, b)
print(int((min_num+max_num)*(max_num-min_num+1)/2))
