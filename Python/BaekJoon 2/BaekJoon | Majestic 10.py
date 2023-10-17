def more_than_10(nums):
    return len([n for n in nums if n >= 10])

def majestic_10(num_lists):
    answers = {0: "zilch", 1: "double", 2: "double-double", 3: "triple-double"}
    return "\n\n".join([f"{' '.join(map(str, nl))}\n{answers[more_than_10(nl)]}" for nl in num_lists])

list_num = [list(map(int, input().split())) for _ in range(int(input()))]
print(majestic_10(list_num))
