def name_that_number(x):
    l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    l2 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if x < 20:
        return l1[x]
    else:
        if x%10 == 0:
            return l2[x//10]
        else:
            return f'{l2[x//10]} {l1[x%10]}'
