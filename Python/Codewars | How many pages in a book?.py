def amount_of_pages(summary):
    if summary < 10:
        return summary
    for i in range(1, summary+1):
        if summary <= 0:
            return i-1
        summary -= len(str(i))
