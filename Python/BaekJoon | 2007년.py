import datetime

m, d = map(int, input().split())
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(days[datetime.date(2007, m, d).weekday()])
