r = ''
while 1:
    try:
        r += input()
    except:
        print(eval(r.replace(',', '+')))
        break
