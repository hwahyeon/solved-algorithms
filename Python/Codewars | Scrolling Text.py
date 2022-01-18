def scrolling_text(text):
    res = []
    l = len(text)
    for i in range(l):
        res.append((text.upper()*2)[i:i+l])
    return res
