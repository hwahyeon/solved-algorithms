for _ in range(int(input())):
    blank = input()
    box = ''
    c = 0
    h, w = map(int, input().split())
    for j in range(h):
        box += input()
    c += box.count('>o<')
    for i in range(len(box)-(2*w)):
        if box[i] == 'v' and box[i+w] == 'o' and box[i+(2*w)] == '^':
                c += 1
    print(c)
