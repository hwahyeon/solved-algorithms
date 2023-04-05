for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    print('Tie') if lt * wt == le * we else print(['Eurecom', 'TelecomParisTech'][lt * wt > le * we])
    
    

##############################
for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    if lt * wt < le * we:
        print("Eurecom")
    elif lt * wt > le * we:
        print("TelecomParisTech")
    else :
        print("Tie")
