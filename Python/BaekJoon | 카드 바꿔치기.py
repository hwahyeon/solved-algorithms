total = int(input())

for i in range(total):
    num = input()
    card1 = input()
    card2 = input()
    if sorted(card1.split()) == sorted(card2.split()):
        print('NOT CHEATER')
    else:
        print('CHEATER')
