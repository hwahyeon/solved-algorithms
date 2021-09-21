def isLeapYear(year):
    return True if (year%4==0 and year%100!=0) or year%400==0 else False
