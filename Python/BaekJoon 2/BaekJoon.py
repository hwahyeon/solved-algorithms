sleep = int(input())
wake = int(input())

if sleep < wake:
    res = wake - sleep
else:
    res = (24 - sleep) + wake

print(res)
