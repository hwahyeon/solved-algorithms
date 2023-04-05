str_ = input().upper()
lst_ = list(set(str_))
res_ = []
for i in lst_:
    res_.append(str_.count(i))

if res_.count(max(res_)) > 1:
    print('?')
else:
    print(lst_[res_.index(max(res_))])
