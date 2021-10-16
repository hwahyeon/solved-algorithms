from datetime import datetime, timedelta

now = datetime.now() - timedelta(hours=9)
print(now.year)
print('%02d'%now.month)
print('%02d'%now.day)
