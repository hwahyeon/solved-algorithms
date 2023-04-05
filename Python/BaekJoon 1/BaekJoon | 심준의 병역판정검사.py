for _ in range(int(input())):
    h, w = map(int, input().split())
    BMI = w/(h*0.01)**2
    if h < 140.1:
        print(6)
    elif h < 146:
        print(5)
    elif h < 159:
        print(4)
    elif h < 161:
        if 16 <= BMI < 35:
            print(3)
        else:
            print(4)
    elif h < 204:
        if 20 <= BMI < 25:
            print(1)
        elif 18.5 <= BMI < 20 or 25 <= BMI < 30:
            print(2)
        elif 16 <= BMI < 18.5 or 30 <= BMI < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)
