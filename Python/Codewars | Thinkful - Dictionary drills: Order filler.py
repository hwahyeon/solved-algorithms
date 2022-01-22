def fillable(stock, merch, n):
    return (merch in stock) and (stock[merch] >= n)
