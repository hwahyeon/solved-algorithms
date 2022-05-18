L, R, A = map(int, input().split())
sum = L + R + A
sub = abs(L - R) - A
print(sum - sub) if sub > 0 else print(sum - (sub%2))
