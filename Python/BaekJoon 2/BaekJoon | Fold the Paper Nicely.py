for _ in range(int(input())):
    w, h, f = map(int, input().split())
    print(f"Data set: {w} {h} {f}")
    
    for _ in range(f):
        if w > h:
            w //= 2
        else:
            h //= 2
    
    if w > h:
        print(f"{w} {h}\n")
    else:
        print(f"{h} {w}\n")
