str_ = input()
lst_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in lst_:
    str_ = str_.replace(i, '0')
print(len(str_))
