a, b = map(int, input().split())
if a == b == 0:
    print("Not a moose")
elif a != b:
    print("Odd " + str(max(a, b)*2))
elif a == b:
    print("Even " + str(b*2))
