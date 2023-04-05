num = int(input())
for i in reversed(range(1, num+1)):
    print(  ( ((2*i-1)*'*').center(2*num-1) ).rstrip()  )
