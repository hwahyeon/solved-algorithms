from datetime import datetime, timedelta

input_date = input().strip()
tentative_date = datetime.strptime(input_date, "%Y-%m-%d")

deadline_date = datetime(2023, 10, 21) - timedelta(days=35)

if tentative_date <= deadline_date:
    print("GOOD")
else:
    print("TOO LATE")
