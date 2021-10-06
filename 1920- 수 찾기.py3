number_N = int(input())
N = set(map(int, input().split()))
number_M = int(input())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print('1')
    else:
        print('0')