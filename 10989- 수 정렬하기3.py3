import sys

test_data = int(sys.stdin.readline())
array = [0] * 10001

for _ in range(test_data):
    n = int(sys.stdin.readline())
    array[n] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
        