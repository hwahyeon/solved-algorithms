def kata_13_december(lst): 
    # Fix this code
    for i in lst[::-1]: 
        if i%2 == 0: 
            lst.remove(i)
    return lst
