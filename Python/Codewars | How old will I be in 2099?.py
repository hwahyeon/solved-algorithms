def calculate_age(year_of_birth, current_year):
    i = str(abs(year_of_birth - current_year))
    if year_of_birth < current_year:
        res = "You are "+i+" years old."
    elif year_of_birth == current_year:
        res = "You were born this very year!"
    else:
        res = "You will be born in "+i+" years."
    return res.replace('1 years', '1 year') if int(i) == 1 else res
