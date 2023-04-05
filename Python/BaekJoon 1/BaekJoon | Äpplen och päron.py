axel, petra = map(int, input().split())
if axel * 7 == petra * 13:
    print("lika")
elif axel * 7 < petra * 13:
    print("Petra")
else:
    print("Axel")
