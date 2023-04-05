lst = input().split('=')
print('YES') if eval(lst[0]) == int(lst[1]) else print('NO')
