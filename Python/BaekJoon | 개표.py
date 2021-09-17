vote = int(input())
str_ = input()

A = str_.count('A')
B = str_.count('B')

if A > B:
    print('A')
elif A == B:
    print('Tie')
else:
    print('B')
