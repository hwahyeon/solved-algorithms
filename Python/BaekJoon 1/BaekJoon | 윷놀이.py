for _ in range(3):
    n = list(map(int, input().split())).count(0)
    print(['E', 'A', 'B', 'C', 'D'][n])
