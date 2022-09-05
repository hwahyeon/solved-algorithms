def cookie(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) is bool:
        return "Who ate the last cookie? It was the dog!"
    else:
        return "Who ate the last cookie? It was Monica!"
