no_need = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
sen = list(input().split())
res = sen[0][0]

for i in sen[1:]:
    if i not in no_need:
        res += i[0]

print(res.upper())
