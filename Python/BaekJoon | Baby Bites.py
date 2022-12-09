n = int(input())
l = list(input().split())
i = 1
r = 0
for j in range(len(l)):
    if l[j] == 'mumble':
        i += 1
    elif int(l[j]) == i:
        i += 1
    else:
        r += 1
print('something is fishy') if r !=0 else print('makes sense')
