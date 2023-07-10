for i in range(int(input())) :
    id = input()
    
    res = sum([int(j) for j in id]) + int(id[10:])*10
    if res > 9999:
        print(str(res % 10000).zfill(4))
    elif res < 1000:
        print(res + 1000)
    else:
        print(res)
