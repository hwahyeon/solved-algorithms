def running_pace(distance, time):
    mm, ss = map(int, time.split(':'))
    n = (mm * 60 + ss)/distance
    if n%60 > 10:
        return f'{int(n//60)}:{int(n%60)}'
    else:
        return f'{int(n//60)}:0{int(n%60)}'
