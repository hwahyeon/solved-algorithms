n = int(input())
lst = [1,2,3]
for _ in range(n):
    a, b = map(int, input().split())
    ch_a, ch_b = lst.index(a), lst.index(b)
    lst[ch_a], lst[ch_b] = lst[ch_b], lst[ch_a]

print(lst[0])
