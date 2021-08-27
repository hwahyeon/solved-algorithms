len = int(input())

for i in range(len):
    a,b = map(int, input().split())
    print("Case #%s: %s + %s = %s"%(i+1, a, b, a+b))
