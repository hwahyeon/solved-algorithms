t = int(input())

lst = [10,
       1,
       [2,4,8,6],
       [3,9,7,1],
       [4,6,4,6],
       5,
       6,
       [7,9,3,1],
       [8,4,2,6],
       [9,1,9,1]]
for _ in range(t):
    a, b = map(int, input().split())
    a = a % 10
    b = b % 4

    if a in [0, 1, 5, 6]:
        print(lst[a])
    else:
        print(lst[a][b-1])
