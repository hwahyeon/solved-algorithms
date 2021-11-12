def number2words(n):
    n_1 = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    n_10 = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    
    if n < 20:
        return n_1[n]
    elif n < 100:
        return n_10[n//10] + '-' + n_1[n%10] if n%10 != 0 else n_10[n//10]
    elif n < 1000:
        if n%100 == 0:
            return number2words(n//100) + ' hundred'
        else:
            return number2words(n//100) + ' hundred ' + number2words(n%100)
    elif n < 10000:
        if n%1000 == 0:
            return number2words(n//1000) + ' thousand'
        elif n%100 == 0:
            return number2words(n//1000) + ' thousand ' + number2words(n%1000//100) + ' hundred'
        else:
            return number2words(n//1000) + ' thousand ' + number2words(n%1000)
    else:
        return number2words(n//1000) + ' thousand ' + number2words(n%1000)
