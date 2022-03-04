def service(score):
    a, b = map(int, score.split(':'))
    if a + b < 40:
        cal = ((a + b) // 5) % 2
    else:
        cal = ((a + b - 40) // 2) % 2

    return 'first' if cal == 0 else 'second'
