n = int(input())
lst_ = list(map(int, input().split()))
m = max(lst_)
for i in range(n):
    lst_[i] = lst_[i]/m*100
print(sum(lst_, 0.0) / len(lst_))
