s1 = set(range(1, int(input())+1))
s2 = set(map(int, input().split()))
print(*s1-s2)
