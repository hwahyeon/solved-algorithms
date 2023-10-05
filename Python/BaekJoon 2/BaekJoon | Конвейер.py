n = int(input())
sum_seq = sum(list(map(int, input().split())))

if sum_seq > 0:
    print("Right")
elif sum_seq < 0:
    print("Left")
else:
    print("Stay")
