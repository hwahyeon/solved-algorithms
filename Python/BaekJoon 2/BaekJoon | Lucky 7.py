def check_lucky(n):
    contains_7 = '7' in str(n)
    divisible_by_7 = n % 7 == 0

    if not contains_7 and not divisible_by_7:
        return 0
    elif not contains_7 and divisible_by_7:
        return 1
    elif contains_7 and not divisible_by_7:
        return 2
    else:
        return 3

print(check_lucky(int(input())))
