n = int(input())
num = int(input())

while num:
    if num % n == 0:
        print(f"{num} is a multiple of {n}.")
    else:
        print(f"{num} is NOT a multiple of {n}.")
    num = int(input())
