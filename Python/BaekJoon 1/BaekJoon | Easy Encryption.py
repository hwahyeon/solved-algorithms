alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(ch):
    if ch in alpha:
        index = alpha.find(ch) + 1
        return str(index).zfill(2)
    elif ch.isdigit():
        return f"#{ch}"
    else:
        return ch

for char in input():
    print(encryption(char), end="")
