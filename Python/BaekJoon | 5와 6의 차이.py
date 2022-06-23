a, b = input().split()
min_num = int(a.replace('6', '5'))+int(b.replace('6', '5'))
max_num = int(a.replace('5', '6'))+int(b.replace('5', '6'))
print(min_num, max_num)
