for _ in range(int(input())):
    blank = input()
    s1, s2 = map(int, input().split())
    sej = list(map(int, input().split()))
    seb = list(map(int, input().split()))
    
    if max(sej) >= max(seb):
        print("S")
    else:
        print("B")


# 개행 문자를 신경 쓰자!!!
