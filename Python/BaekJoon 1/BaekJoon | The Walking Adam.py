for _ in range(int(input())):
    r = 0
    for i in input():
        if i == "U":
            r += 1
        else:
            break
    print(r)
