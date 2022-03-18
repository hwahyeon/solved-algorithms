i = 0
while 1:
    n1 = 3*int(input())
    i += 1
    if n1 == 0:
        break
    elif n1 % 2 == 0:
        print("%d. even %d" %(i, (1.5*n1)//9))
    else:
        print("%d. odd %d" % (i, (1.5*(n1+1))//9))
