def solution(price, money, count):
    res_=0
    for i in range(count):
        res_ += price*(i+1)
    if res_ < money:
        return 0
    else :
        return (res_ - money)
