def points(games):
    point = 0
    for i in games:
        x, y = map(int, i.split(':'))
        if x > y:
            point += 3
        elif x == y:
            point += 1
    return point
