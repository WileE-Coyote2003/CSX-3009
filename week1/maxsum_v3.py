# Name: Thwin Htoo Aung
# ID: 6612109
# Section: 541

import time

start = time.process_time()

def MaxSum(x):
    max_sum = current_sum = x[0]
    for num in x[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

x = list(map(int, input().split()))

result = MaxSum(x)

finish = time.process_time()

print("Maximum Subarray Sum:", result)
print("Time taken:", finish - start)