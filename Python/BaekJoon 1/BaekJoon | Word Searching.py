s = input()
r = 0
while 1:
    try:
        r += input().count(s)
    except EOFError:
        break
print(r)
