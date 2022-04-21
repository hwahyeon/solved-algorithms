def fibonacci(n: int) -> int:
    n1, n2 = 0, 1
    for _ in range(n):
        n1, n2 = n2, n1 + n2
    return n1
