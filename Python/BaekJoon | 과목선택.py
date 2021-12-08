t = []
for _ in range(4):
    t.append(int(input()))

t = sum(sorted(t)[1:4])
E = int(input())
F = int(input())

print(t+E) if E > F else print(t+F)
