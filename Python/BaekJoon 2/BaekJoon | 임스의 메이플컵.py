n, v1, v2 = map(int, input().split())

if n >= 1000:
    if v1 >= 8000 or v2 >= 260:
        print("Very Good")
    else:
        print("Good")
else:
    print("Bad")
