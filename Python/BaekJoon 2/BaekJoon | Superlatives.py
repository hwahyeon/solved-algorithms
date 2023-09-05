K = int(input())

for i in range(K):
    E, A = map(int, input().split())
    factor = E / A
    
    res = "Data Set " + str(i+1) + ":\n"
    
    if factor <= 1:
        res += "no drought"
    else:
        count_mega = 0
        while factor > 1:
            factor /= 5
            count_mega += 1

        if count_mega == 1:
            res += "drought"
        else:
            res += " ".join(["mega"] * (count_mega - 1)) + " drought"
    
    print(res)
    print()
