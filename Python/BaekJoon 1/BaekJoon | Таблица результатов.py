n, m = map(int, input().split())

tasks = 0

for _ in range(n):
    row = input().strip()
    
    if '+' in row:
        tasks += 1

print(tasks)
