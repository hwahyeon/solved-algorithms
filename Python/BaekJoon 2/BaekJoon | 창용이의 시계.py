import sys

def adjust_time(h, m, s, adjustment):
    total_seconds = h * 3600 + m * 60 + s + adjustment
    total_seconds = (total_seconds + 86400) % 86400
    return total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60

h, m, s = map(int, sys.stdin.readline().split())

for _ in range(int(sys.stdin.readline())):
    command = list(map(int, sys.stdin.readline().split()))
    
    if command[0] == 3:
        print(h, m, s)
    else:
        operation, value = command[0], command[1]
        adjustment = value if operation == 1 else -value
        h, m, s = adjust_time(h, m, s, adjustment)
