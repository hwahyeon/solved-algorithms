r = []
N, B, H, W = map(int, input().split())
for _ in range(H):
    P = int(input())
    week = list(map(int, input().split()))
    if max(week) >= N:
        if (N * P) <= B:
            r.append(P * N)
print(min(r)) if len(r) != 0 else print("stay home")
