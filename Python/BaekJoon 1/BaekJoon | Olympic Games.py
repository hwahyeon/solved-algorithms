def olympic(year):
    if year % 4 == 0 and year >= 1896:
        if 1914 <= year <= 1918 or 1939 <= year <= 1945:
            return f"{year} Games cancelled"
        elif year > 2020:
            return f"{year} No city yet chosen"
        else:
            return f"{year} Summer Olympics"
    else:
        return f"{year} No summer games"

while True:
    year = int(input())
    
    if year == 0:
        break
    
    print(olympic(year))
