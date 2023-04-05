for _ in range(int(input())):
    s = input()
    g, b = s.lower().count("g"), s.lower().count("b")
    if g > b:
        print(f'{s} is GOOD')
    elif g == b:
        print(f'{s} is NEUTRAL')
    else:
        print(f'{s} is A BADDY')
