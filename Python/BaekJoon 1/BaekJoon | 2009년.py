import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day, month = map(int, input().split())

print(days[datetime.date(2009, month, day).weekday()])
