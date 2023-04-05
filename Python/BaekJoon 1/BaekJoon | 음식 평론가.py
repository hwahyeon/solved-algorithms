n, m = map(int, input().split())

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

print(m - GCD(n, m))
