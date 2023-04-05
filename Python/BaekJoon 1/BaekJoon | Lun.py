def card_checker(n, lst):
    lst = list(map(int, lst))
    end = lst[-1]
    lst = lst[::-1]
    for i in range(1, n + 1):
        if i % 2 == 0:
            lst[i - 1] = lst[i - 1] * 2
            if lst[i - 1] > 9:
                lst[i - 1] = 1 + lst[i - 1] % 10
    return sum(lst[1:]) * 9 % 10 == end

n = int(input())
card = list(input())
x = card.index('x')
for i in range(10):
    card[x] = i
    if card_checker(n, card):
        print(i)
        break
