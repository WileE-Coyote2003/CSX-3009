# Name: Thwin Htoo Aung
# ID: 6612109
# Section: 541

import time

start = time.process_time()

def accumulate_list(x):
    acc = [0] * len(x)
    acc[0] = x[0]
    for i in range(1, len(x)):
        acc[i] = acc[i - 1] + x[i]
    return acc

def Sum(acc, i, j):
    if i == 0:
        return acc[j]
    else:
        return acc[j] - acc[i - 1]

def MaxSum(x):
    n = len(x)
    acc = accumulate_list(x)
    max_sum = -float('inf')
    for i in range(n):
        for j in range(i, n):
            s = Sum(acc, i, j)
            if s > max_sum:
                max_sum = s
    return max_sum

x = list(map(int, input().split()))

result = MaxSum(x)

finish = time.process_time()
print("Maximum Subarray Sum:", result)
print("Time taken:", finish - start)