T1, F1, S1, P1, C1 = list(map(int, input().split()))
T2, F2, S2, P2, C2 = list(map(int, input().split()))
a = T1 * 6 + F1 * 3 + S1 * 2 + P1 + C1 * 2
b = T2 * 6 + F2 * 3 + S2 * 2 + P2 + C2 * 2
print(a, b)
