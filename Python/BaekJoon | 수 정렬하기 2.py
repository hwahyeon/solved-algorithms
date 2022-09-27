import sys

l = []
for _ in range(int(input())):
    l.append(int(sys.stdin.readline()))
l.sort()

for i in l:
    print(i)
