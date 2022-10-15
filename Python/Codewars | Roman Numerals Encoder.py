def solution(n):
    r = []
    l = list(map(int, str(n)[::-1]))
    roman = [['I', 'V'],
             ['X', 'L'],
             ['C', 'D'],
             ['M', 'M']]
    for i in range(len(l)):
        if l[i] < 4:
            r.append(roman[i][0] * l[i])
        elif l[i] == 4:
            r.append(roman[i][0] + roman[i][1])
        elif l[i] == 5:
            r.append(roman[i][1])
        elif l[i] == 9:
            r.append(roman[i][0] + roman[i+1][0])
        else:
            r.append(roman[i][1] + roman[i][0] * (l[i] - 5))
    return ''.join(r[::-1])
