n = int(input())
l = list(map(int, input().split()))
print('yes') if sum(l)%3 == 0 else print('no')
