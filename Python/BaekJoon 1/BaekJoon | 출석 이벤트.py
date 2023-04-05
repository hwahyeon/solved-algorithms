N = int(input())
price = int(input())
sale = [0]

if N >= 5 :
    sale.append(500)
if N >= 10 :
    sale.append(price // 10)
if N >= 15 :
    sale.append(2000)
if N >= 20 :
    sale.append(price // 4)

r = price - max(sale)
if r < 0 :
    r = 0
print(r)
