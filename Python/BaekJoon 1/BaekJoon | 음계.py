l = list(map(int, input().split()))
 
if l == sorted(l):
    print('ascending')
elif l == sorted(l)[::-1]:
    print('descending')
else:
    print('mixed')
