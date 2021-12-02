def test_it(a, b):
    return sum([int(i) for i in str(a)]) * sum([int(i) for i in str(b)])
