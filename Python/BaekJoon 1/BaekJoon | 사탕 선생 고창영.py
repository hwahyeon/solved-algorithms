n = int(input())

for i in range(n):
    candy = 0
    input()
    student = int(input())
    for j in range(student):
        candy += int(input())
    print('YES') if candy%student == 0 else print('NO')
