n = int(input())

for _ in range(n):
    uniform_nums = list(map(int, input().split()))

    is_zack = False
    is_mack = False

    for num in uniform_nums:
        print(num, end=" ")
        if num == 17:
            is_zack = True
        if num == 18:
            is_mack = True
    print()

    if is_zack and is_mack:
        print("both")
    elif is_zack:
        print("zack")
    elif is_mack:
        print("mack")
    else:
        print("none")

    if _ != n - 1:
        print()
