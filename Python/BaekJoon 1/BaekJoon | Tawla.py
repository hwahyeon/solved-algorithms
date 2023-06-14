for i in range(int(input())):
    a, b = map(int, input().split())
    
    l =  ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
    
    if a == b:
        res = ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"][a-1]
    elif min(a, b) == 5 and max(a, b) == 6:
        res = 'Sheesh Beesh'
    else:
        res = l[max(a, b) - 1] + ' ' + l[min(a, b) - 1]
    print(f'Case {i+1}: {res}')
