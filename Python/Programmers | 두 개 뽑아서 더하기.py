import itertools

def solution(numbers):
    if len(numbers) == 1 or len(numbers) == 0:
        return numbers
    else:
        res1 = list(itertools.permutations(numbers,2))
        res2 = []
        for i in res1:
            res2.append(i[0]+i[1])
        return sorted(list(set(res2)))
