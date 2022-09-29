def draw(n):
    heart = ''
    heart += ('◢'+'■'*(n//2-2)+'◣')*2+'\n'
    for _ in range(n//6):
        heart += '■'*n+'\n'
    for i in reversed(range(n//2)):
        heart += '\u2003'*(n//2-i-1)+'◥' +'■'*(i*2) + '◤'+'\u2003'*(n//2-i-1)+'\n'
    return heart[:-1]
