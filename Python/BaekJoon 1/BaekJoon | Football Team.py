while 1:
    try:
        n = input()
        print(n.translate(str.maketrans('ieIE','eiEI')))
    except EOFError:
        break
