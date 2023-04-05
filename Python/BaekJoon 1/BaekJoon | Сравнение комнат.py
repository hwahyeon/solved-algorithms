a, b, c, d = map(int, input().split())
print('E') if a * b == c * d else print(['M', 'P'][a * b < c * d])
